/**
 * shared/deal-store.js
 * 부동산이즈두산공인중개사사무소 - 공통 거래 데이터 저장소 및 워크플로우 연동 모듈
 * 
 * [엑셀 매매약정서 자동화 양식(매매약정서 + 별지) 기반 완벽 동기화 버전]
 * - 매매약정서(agreement/)와 토지거래허가신청서(toji-permit/) 간 거래 데이터 공유
 * - 1페이지 본문(약정금, 이행약정, 당사자 및 공인중개사 날인) 및 2페이지 별지(대금지급표, 특약사항, 약정금 영수증) 완벽 지원
 * - localStorage ('realty_deals') 기반 CRUD & JSON 백업/복원
 */

(function (window) {
  'use strict';

  const STORAGE_KEY = 'realty_deals';

  // 기본 공인중개사 고정 정보 (엑셀 서식 기준)
  const DEFAULT_AGENT = {
    office: '부동산이즈두산공인중개사사무소',
    name: '백 근 영',
    regNo: '41173-2025-00028',
    tel: '031-388-7704',
    phone: '010-5851-2693',
    addr: '경기도 안양시 동안구 평촌대로179번길 39 104호'
  };

  // 거래 진행 상태 정의 (라이프사이클)
  const DEAL_STAGES = {
    agreement_signed: {
      key: 'agreement_signed',
      label: '가계약 완료',
      color: '#d97706',
      bgColor: '#fef3c7',
      badgeClass: 'badge-amber',
      nextAction: '토지거래허가 신청서 구청 접수'
    },
    permit_submitted: {
      key: 'permit_submitted',
      label: '허가신청 접수',
      color: '#2563eb',
      bgColor: '#dbeafe',
      badgeClass: 'badge-blue',
      nextAction: '구청 심사 대기 (통상 15일 이내 처리)'
    },
    permit_approved: {
      key: 'permit_approved',
      label: '허가증 교부',
      color: '#059669',
      bgColor: '#d1fae5',
      badgeClass: 'badge-emerald',
      nextAction: '★ 허가일로부터 7일 이내 본매매계약 체결 필수!'
    },
    contract_signed: {
      key: 'contract_signed',
      label: '본계약 체결',
      color: '#4f46e5',
      bgColor: '#e0e7ff',
      badgeClass: 'badge-indigo',
      nextAction: '중도금/잔금 지급 및 4개월 내 이전등기'
    },
    deal_completed: {
      key: 'deal_completed',
      label: '잔금/이전 완료',
      color: '#475569',
      bgColor: '#f1f5f9',
      badgeClass: 'badge-slate',
      nextAction: '2년 실거주 이용의무 사후 관리'
    }
  };

  const DEFAULT_CO_AGENT = {
    enabled: false,
    office: '',
    name: '',
    regNo: '',
    tel: '',
    addr: ''
  };

  const PRESETS_STORAGE_KEY = 'realty_complex_presets';
  const CLAUSE_STORAGE_KEY = 'realty_clause_templates';

  const DEFAULT_CLAUSE_TEMPLATES = [
    {
      id: 'clean',
      name: '템플릿 1: 권리하자없음 기본',
      chipLabel: '템플릿 1: 권리하자없음 기본',
      content: `2. 등기사항전부증명서상 을구 기재내용 없음으로 권리상 하자없음을 확인하였으며, 매도인은 잔금일까지 소유권의 행사를 제한하는 일체의 제한물권을 설정하지 않기로 한다.

3. 현 시설물 상태의 약정이며, 매수인 직접 현장방문하여 확인한 후 토지거래허가를 득하기 위한 약정임을 인지하고 쌍방 합의하에 진행하는 약정이다.

4. 본 매매약정금은 계약금이 아니므로, 매매계약 체결 시 기지급한 약정금 전액을 반환한 후 계약금을 별도로 지급한다.

5. 토지거래 허가 후 매수약정인은 허가일로부터 4개월 이내 취득(등기)하고 취득일로부터 이용의무(2년 실거주)를 이행해야함을 인지하고 진행하는 약정이다. 다만, 주택 취득일이 그보다 빠를 경우 해당 토지 취득일로부터 이용의무를 이행하여야 한다.

6. 계약서는 부동산거래허가를 득한후 협의된 날 작성하며, 확인설명서도 계약서 작성시 함께 작성, 교부하기로 한다.

7. 기타사항은 계약시 협의하기로 하며, 일방 변심에 의해 계약파기시 중개보수는 지불하기로 한다.`
    },
    {
      id: 'mortgage',
      name: '템플릿 2: 근저당권 말소조건',
      chipLabel: '템플릿 2: 근저당권 말소조건',
      content: `2. 본 약정은 목적 부동산의 공부 및 현 시설물 상태를 현장에서 확인하고, 관련 제반 사항을 포괄적으로 인지한 상태에서 현존하는 상태 그대로를 인도하는 조건의 매매약정이다. (매수약정인이 소재지 직접 방문 확인함)

3. 등기사항전부증명서상 을구 근저당권(채권최고액 등) 설정된 상태로 약정하며, 매도약정인은 잔금일까지 전액 상환 및 말소하기로 하고, 소유권의 행사를 제한하는 일체의 제한물권을 추가로 설정하지 않기로 한다.

4. 본 약정 대상 아파트의 하자담보책임은 잔금 당일까지는 매도약정인 책임, 잔금 익일부터는 매수약정인 책임으로 협의한다. (단, 노후화로 인한 가벼운 결로 및 곰팡이 등은 매매약정금액에 반영된 것으로 보고 하자로 보지 아니한다.)

5. 토지거래 허가 후 매수약정인은 허가일로부터 4개월 이내 취득(등기)하고 취득일로부터 이용의무(2년 실거주)를 이행해야함을 인지하고 진행하는 약정이다.

6. 본 매매계약(전자계약) 체결 시에 매수 약정인은 계약금 전액을 지급하고, 매도 약정인은 수령한 약정금 전액을 매수 약정인에게 반환하기로 한다.

7. 양 당사자는 토지거래허가 신청 및 본계약 체결을 위한 개인정보 수집·이용에 동의한다.`
    },
    {
      id: 'seizure',
      name: '템플릿 3: 가압류 공탁해지',
      chipLabel: '템플릿 3: 가압류 공탁해지',
      content: `2. 본 약정은 목적 부동산의 공부 및 현 시설물 상태를 현장에서 확인하고, 관련 제반 사항을 포괄적으로 인지한 상태에서 현존하는 상태 그대로를 인도하는 조건의 매매약정이다. (매수약정인이 소재지 직접 방문 확인함)

3. 등기사항전부증명서상 갑구 가압류 및 을구 근저당권 설정 상태를 확인함. 매도약정인은 중도금 지급일에 갑구 가압류 해지를 위한 지정계좌(또는 법원 공탁계좌)를 매수약정인에게 제공하고, 중도금 중 가압류 해지 필요금액을 매수약정인이 직접 해당 계좌에 입금하여 완납 처리 후 10일 이내 말소등기를 완료하기로 한다. 을구 근저당권은 잔금일까지 전액 상환 말소한다.

4. 본 약정 대상 아파트의 중대한 하자(누수 등) 발생 시 잔금일 기준 매도약정인 책임, 잔금일 이후 매수약정인 책임으로 협의한다.

5. 토지거래 허가 후 매수약정인은 허가일로부터 4개월 이내 취득(등기)하고 취득일로부터 이용의무(2년 실거주)를 성실히 이행한다.

6. 본 매매계약 체결 시 매수 약정인은 계약금 전액을 지급하고, 매도 약정인은 수령한 약정금 전액을 매수 약정인에게 반환하기로 한다.

7. 추가사항은 본계약 체결 시 상호 협의하여 정하기로 한다.`
    }
  ];

  const DEFAULT_COMPLEX_PRESETS = [
    {
      id: 'mokryeon_2',
      name: '목련두산 2단지',
      chipLabel: '목련두산 2단지 (1056)',
      dong: '호계동',
      jibunMain: '1056',
      jibunSub: '',
      complex: '목련두산아파트',
      roadAddr: '경기도 안양시 동안구 동안로 120',
      landAddr: '경기도 안양시 동안구 호계동 1056',
      bldAddr: '경기도 안양시 동안구 동안로 120 목련두산아파트',
      dongNum: '201',
      hoNum: '1502',
      bldUnit: '제201동 제1502호',
      totalLand: '56123.4',
      ratioDen: '56123.4',
      ratioNum: '51.84',
      landRatioStr: '56123.4분의 51.84',
      exclusiveArea: '84.95',
      officialPrice: '4500000',
      yongdo: '제3종일반주거지역',
      bldStructure: '철근콘크리트조',
      bldUsage: '아파트',
      bldType: '공동주택(아파트)'
    },
    {
      id: 'mokryeon_3',
      name: '목련우성 3단지',
      chipLabel: '목련우성 3단지 (1052-3)',
      dong: '호계동',
      jibunMain: '1052',
      jibunSub: '3',
      complex: '목련우성아파트',
      roadAddr: '경기도 안양시 동안구 평촌대로 180',
      landAddr: '경기도 안양시 동안구 호계동 1052-3',
      bldAddr: '경기도 안양시 동안구 호계동 1052-3 목련아파트',
      dongNum: '308',
      hoNum: '506',
      bldUnit: '제308동 제506호',
      totalLand: '30467.9',
      ratioDen: '30467.9',
      ratioNum: '35.376',
      landRatioStr: '30467.9분의 35.376',
      exclusiveArea: '56.7',
      officialPrice: '4500000',
      yongdo: '제3종일반주거지역',
      bldStructure: '철근콘크리트조',
      bldUsage: '아파트',
      bldType: '공동주택(아파트)'
    },
    {
      id: 'mokryeon_5',
      name: '목련선경 5단지',
      chipLabel: '목련선경 5단지 (1053)',
      dong: '호계동',
      jibunMain: '1053',
      jibunSub: '',
      complex: '목련선경아파트',
      roadAddr: '경기도 안양시 동안구 동안로 110',
      landAddr: '경기도 안양시 동안구 호계동 1053',
      bldAddr: '경기도 안양시 동안구 동안로 110 목련선경아파트',
      dongNum: '502',
      hoNum: '801',
      bldUnit: '제502동 제801호',
      totalLand: '31245.0',
      ratioDen: '31245.0',
      ratioNum: '42.15',
      landRatioStr: '31245.0분의 42.15',
      exclusiveArea: '74.2',
      officialPrice: '4500000',
      yongdo: '제3종일반주거지역',
      bldStructure: '철근콘크리트조',
      bldUsage: '아파트',
      bldType: '공동주택(아파트)'
    },
    {
      id: 'mokryeon_6',
      name: '목련두산 6단지',
      chipLabel: '목련두산 6단지 (1054-6)',
      dong: '호계동',
      jibunMain: '1054',
      jibunSub: '6',
      complex: '목련두산아파트',
      roadAddr: '경기도 안양시 동안구 평촌대로179번길 27',
      landAddr: '경기도 안양시 동안구 호계동 1054-6',
      bldAddr: '경기도 안양시 동안구 평촌대로179번길 27 목련두산아파트',
      dongNum: '603',
      hoNum: '402',
      bldUnit: '제603동 제402호',
      totalLand: '29263.2',
      ratioDen: '29263.2',
      ratioNum: '54.395',
      landRatioStr: '29263.2분의 54.395',
      exclusiveArea: '101.94',
      officialPrice: '4500000',
      yongdo: '제3종일반주거지역',
      bldStructure: '철근콘크리트조',
      bldUsage: '아파트',
      bldType: '공동주택(아파트)'
    }
  ];

  const DealStore = {
    STORAGE_KEY: STORAGE_KEY,
    PRESETS_STORAGE_KEY: PRESETS_STORAGE_KEY,
    DEFAULT_AGENT: DEFAULT_AGENT,
    DEFAULT_CO_AGENT: DEFAULT_CO_AGENT,
    DEAL_STAGES: DEAL_STAGES,
    DEFAULT_COMPLEX_PRESETS: DEFAULT_COMPLEX_PRESETS,
    DEFAULT_CLAUSE_TEMPLATES: DEFAULT_CLAUSE_TEMPLATES,
    CLAUSE_STORAGE_KEY: CLAUSE_STORAGE_KEY,

    getComplexPresets: function () {
      try {
        const raw = localStorage.getItem(PRESETS_STORAGE_KEY);
        if (raw) {
          const parsed = JSON.parse(raw);
          if (Array.isArray(parsed) && parsed.length > 0) return parsed;
        }
      } catch (e) {
        console.error('[DealStore] getComplexPresets error:', e);
      }
      return JSON.parse(JSON.stringify(DEFAULT_COMPLEX_PRESETS));
    },

    saveComplexPresets: function (list) {
      try {
        localStorage.setItem(PRESETS_STORAGE_KEY, JSON.stringify(list));
        return true;
      } catch (e) {
        console.error('[DealStore] saveComplexPresets error:', e);
        return false;
      }
    },

    resetComplexPresets: function () {
      try {
        localStorage.removeItem(PRESETS_STORAGE_KEY);
      } catch (e) { }
      return JSON.parse(JSON.stringify(DEFAULT_COMPLEX_PRESETS));
    },

    getClauseTemplates: function () {
      try {
        const raw = localStorage.getItem(CLAUSE_STORAGE_KEY);
        if (raw) {
          const parsed = JSON.parse(raw);
          if (Array.isArray(parsed) && parsed.length > 0) return parsed;
        }
      } catch (e) {
        console.error('[DealStore] getClauseTemplates error:', e);
      }
      return JSON.parse(JSON.stringify(DEFAULT_CLAUSE_TEMPLATES));
    },

    saveClauseTemplates: function (list) {
      try {
        localStorage.setItem(CLAUSE_STORAGE_KEY, JSON.stringify(list));
        return true;
      } catch (e) {
        console.error('[DealStore] saveClauseTemplates error:', e);
        return false;
      }
    },

    resetClauseTemplates: function () {
      try {
        localStorage.removeItem(CLAUSE_STORAGE_KEY);
      } catch (e) { }
      return JSON.parse(JSON.stringify(DEFAULT_CLAUSE_TEMPLATES));
    },

    /**
     * 신규 거래 기본 데이터 템플릿 생성 (순수 빈 서식)
     */
    createEmptyDeal: function () {
      const today = new Date();
      const yyyy = today.getFullYear();
      const mm = String(today.getMonth() + 1).padStart(2, '0');
      const dd = String(today.getDate()).padStart(2, '0');
      const todayStr = `${yyyy}-${mm}-${dd}`;

      return {
        id: 'deal_' + Date.now() + '_' + Math.random().toString(36).substring(2, 7),
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
        dealDate: todayStr, // 약정일
        status: 'agreement_signed', // 거래 진행 상태
        title: '',          // 제목

        // 1. 부동산의 표시 (토지 및 건축물)
        property: {
          // 토지
          landAddr: '',
          landAreaTotal: '',
          landRatioNum: '',
          landRatioDen: '',
          landRatioStr: '',
          landCategoryLegal: '대',
          landCategoryActual: '대',
          landUnitPrice: 0,
          zoning: '제3종일반주거지역',
          landUseStatus: '주거용',
          rightsStatus: '소유권',

          // 건축물
          bldAddr: '',
          exclusiveArea: '',
          commonArea: '',
          bldStructure: '철근콘크리트조',
          bldUsage: '아파트',
          bldType: '공동주택',
          bldDetail: '아파트',

          // 공적장부 분해 항목 (토지거래허가서 바인딩용)
          sido: '경기도',
          sgg: '안양시 동안구',
          dong: '호계동',
          jibunMain: '',
          jibunSub: '',
          jibunExtra: '',
          complex: '',
          dongNum: '',
          hoNum: '',
          roadAddr: '',
          addrFull: '',
          landShare: ''
        },

        // 2. 당사자 정보 (소유자 및 매수약정인 각각 명의자1, 명의자2 공동명의 지원)
        parties: {
          sellers: [
            {
              name: '',
              rrn: '',
              tel: '',
              addr: '',
              share: '1/1'
            }
          ],
          buyers: [
            {
              name: '',
              rrn: '',
              tel: '',
              addr: '',
              share: '1/1'
            }
          ]
        },

        // 3. 계약내용 및 대금 지급일정
        financial: {
          // 약정금
          tempDeposit: 0,        // 매매약정금
          tempDepositDate: todayStr,    // 약정일
          isTempSplit: false,           // 분할입금 여부
          tempDeposit1: 0,       // 1차 약정금
          tempDeposit1Date: todayStr,   // 1차 입금일
          tempDeposit2: 0,              // 2차 약정금
          tempDeposit2Date: '',         // 2차 입금일
          tempDepositAccount: '',       // 입금계좌

          // 매매대금 및 지급일정
          totalPrice: 0,        // 매매대금
          contractDeposit: 0,   // 계약금
          contractSchedule: '토지거래허가후 7일이내', // 계약예정일
          contractDate: '',
          midPayment: 0,        // 중도금(1차)
          midDate: '',                  // 중도금(1차) 예정일
          midNote: '예정',
          midPayment2: 0,               // 중도금(2차)
          midDate2: '',                 // 중도금(2차) 예정일
          midNote2: '예정',
          balance: 0,           // 잔금
          balanceDate: '',    // 잔금예정일
          balanceNote: '이내로 협의',
          specialTerms: ''
        },

        // 4. 토지거래허가 전용 항목
        permit: {
          rightKind: '소유권',
          rightAction: '취득',
          transferType: '유상',
          purpose: '주거용 (세대원 전원 실거주 자가주택 취득)',
          residents: '',
          regDate: '',
          moveInDate: '',
          funding: {
            deposit: 0,
            stocks: 0,
            gift: 0,
            realestate: 0,
            loanBank: 0,
            borrow: 0
          },
          usagePlan: {
            householdCount: 0,
            currentHomeCount: 0,
            dispositionPlan: '',
            actualLiving: '본인 및 세대원 전원 실거주 예정'
          }
        },

        // 5. 공인중개사 정보
        agent: Object.assign({}, DEFAULT_AGENT),
        coAgent: Object.assign({}, DEFAULT_CO_AGENT)
      };
    },

    /**
     * 저장된 모든 거래 목록 반환 (최신 수정순)
     */
    listDeals: function () {
      try {
        const raw = localStorage.getItem(STORAGE_KEY);
        if (!raw) return [];
        const list = JSON.parse(raw);
        if (!Array.isArray(list)) return [];
        return list.sort(function (a, b) {
          const tA = new Date(a.updatedAt || a.createdAt || 0).getTime();
          const tB = new Date(b.updatedAt || b.createdAt || 0).getTime();
          return tB - tA;
        });
      } catch (e) {
        console.error('[DealStore] listDeals error:', e);
        return [];
      }
    },

    /**
     * 거래 단건 조회
     */
    getDeal: function (id) {
      if (!id) return null;
      const list = this.listDeals();
      return list.find(function (d) { return d.id === id; }) || null;
    },

    /**
     * 거래 저장 (신규 추가 또는 기존 업데이트)
     */
    saveDeal: function (dealData) {
      if (!dealData) throw new Error('저장할 거래 데이터가 없습니다.');
      const list = this.listDeals();

      if (!dealData.id) {
        dealData.id = 'deal_' + Date.now() + '_' + Math.random().toString(36).substring(2, 7);
      }

      dealData.updatedAt = new Date().toISOString();
      dealData.status = dealData.status || 'agreement_signed';
      if (!dealData.createdAt) {
        dealData.createdAt = dealData.updatedAt;
      }

      // 제목 자동 보정
      const p = dealData.property || {};
      let unitPart = '';
      if (p.dongNum && p.hoNum) unitPart = `${p.dongNum}동${p.hoNum}호`;
      else if (p.dongNum) unitPart = `${p.dongNum}동`;
      else if (p.hoNum) unitPart = `${p.hoNum}호`;

      let titleParts = [];
      if (dealData.dealDate) titleParts.push(dealData.dealDate.replace(/-/g, ''));
      if (p.dong) titleParts.push(p.dong);
      if (p.complex) titleParts.push(p.complex);
      if (unitPart) titleParts.push(unitPart);

      dealData.title = titleParts.join('_') || ('거래_' + dealData.id);

      const existingIndex = list.findIndex(function (d) { return d.id === dealData.id; });
      if (existingIndex >= 0) {
        list[existingIndex] = dealData;
      } else {
        list.unshift(dealData);
      }

      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(list));
      } catch (e) {
        console.error('[DealStore] saveDeal localStorage error:', e);
        throw new Error('localStorage 저장 용량 초과 또는 권한 오류가 발생했습니다.');
      }

      return dealData;
    },

    /**
     * 거래 삭제
     */

    /**
     * 거래 진행 상태 변경 (예: 가계약 -> 허가접수 -> 허가완료 -> 본계약 -> 잔금완료)
     */
    updateDealStatus: function (dealId, newStatus, extraData = {}) {
      const deal = this.getDeal(dealId);
      if (!deal) return null;
      if (!DEAL_STAGES[newStatus]) {
        console.warn('[DealStore] Unknown deal status:', newStatus);
      }
      deal.status = newStatus;
      deal.statusUpdatedAt = new Date().toISOString();
      if (newStatus === 'permit_approved' && !deal.permitApprovedDate) {
        deal.permitApprovedDate = new Date().toISOString().split('T')[0];
      }
      if (extraData && typeof extraData === 'object') {
        Object.assign(deal, extraData);
      }
      return this.saveDeal(deal);
    },

    /**
     * 허가완료(permit_approved) 상태일 때 7일 이내 본계약 D-Day 계산
     */
    getPermitDDay: function (deal) {
      if (!deal || deal.status !== 'permit_approved') return null;
      const refDateStr = deal.permitApprovedDate || (deal.statusUpdatedAt ? deal.statusUpdatedAt.split('T')[0] : null);
      if (!refDateStr) return null;
      const refDate = new Date(refDateStr + 'T00:00:00');
      const now = new Date();
      now.setHours(0, 0, 0, 0);
      const diffMs = now.getTime() - refDate.getTime();
      const passedDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));
      const remainingDays = 7 - passedDays;
      return {
        approvedDate: refDateStr,
        passedDays: passedDays,
        remainingDays: remainingDays,
        isOverdue: remainingDays < 0,
        isDueToday: remainingDays === 0
      };
    },

    /**
     * 주소 및 대지권비율 스마트 분해 유틸리티 (매매약정서 ↔ 토지거래허가서 공통)
     */
    parseAddressAndRatio: function (landAddr, bldAddr, ratioStr) {
      const result = {
        sido: '경기도',
        sgg: '안양시 동안구',
        dong: '',
        jibunMain: '',
        jibunSub: '',
        complex: '',
        dongNum: '',
        hoNum: '',
        ratioDen: 0,
        ratioNum: 0,
        landShare: 0
      };

      const source = landAddr || bldAddr || '';
      const mDong = source.match(/([가-힣\d]+동)\s+(\d+)(?:-(\d+))?/);
      if (mDong) {
        result.dong = mDong[1];
        result.jibunMain = mDong[2];
        result.jibunSub = mDong[3] || '';
      }

      if (bldAddr) {
        const mCplx = bldAddr.match(/([가-힣\w]+(?:아파트|마을|단지|빌라))/);
        if (mCplx) result.complex = mCplx[1];

        const mDongNum = bldAddr.match(/제?(\d+)\s*동/);
        if (mDongNum) result.dongNum = mDongNum[1];

        const mHoNum = bldAddr.match(/제?(\d+)\s*호/);
        if (mHoNum) result.hoNum = mHoNum[1];
      }

      if (ratioStr) {
        const mRatio = ratioStr.match(/([\d\.]+)\s*(?:분의|\/)\s*([\d\.]+)/);
        if (mRatio) {
          result.ratioDen = parseFloat(mRatio[1]) || 0;
          result.ratioNum = parseFloat(mRatio[2]) || 0;
          result.landRatioDen = result.ratioDen;
          result.landRatioNum = result.ratioNum;
          result.landShare = result.ratioNum;
        }
      }

      return result;
    },

    deleteDeal: function (id) {
      if (!id) return false;
      const list = this.listDeals().filter(function (d) { return d.id !== id; });
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(list));
        return true;
      } catch (e) {
        console.error('[DealStore] deleteDeal error:', e);
        return false;
      }
    },

    /**
     * JSON 내보내기
     */
    exportJson: function (dealId) {
      let dataToExport;
      let filename;

      if (dealId) {
        const deal = this.getDeal(dealId);
        if (!deal) {
          alert('해당 거래를 찾을 수 없습니다.');
          return;
        }
        dataToExport = deal;
        filename = this.generateStandardFileName(deal, '거래데이터') + '.json';
      } else {
        const list = this.listDeals();
        dataToExport = {
          version: '1.2',
          exportedAt: new Date().toISOString(),
          agency: DEFAULT_AGENT.office,
          deals: list
        };
        const todayStr = new Date().toISOString().slice(0, 10).replace(/-/g, '');
        filename = `${todayStr}_부동산이즈_전체거래백업.json`;
      }

      const jsonStr = JSON.stringify(dataToExport, null, 2);
      const blob = new Blob([jsonStr], { type: 'application/json;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    },

    /**
     * JSON 가져오기
     */
    importJson: function (fileOrString) {
      const self = this;
      return new Promise(function (resolve, reject) {
        if (typeof fileOrString === 'string') {
          try {
            const parsed = JSON.parse(fileOrString);
            const count = self._mergeImportedData(parsed);
            resolve(count);
          } catch (e) {
            reject(new Error('JSON 파싱 실패: ' + e.message));
          }
        } else if (fileOrString instanceof File) {
          const reader = new FileReader();
          reader.onload = function (e) {
            try {
              const parsed = JSON.parse(e.target.result);
              const count = self._mergeImportedData(parsed);
              resolve(count);
            } catch (err) {
              reject(new Error('파일 파싱 실패: ' + err.message));
            }
          };
          reader.onerror = function () {
            reject(new Error('파일 읽기 오류가 발생했습니다.'));
          };
          reader.readAsText(fileOrString, 'UTF-8');
        } else {
          reject(new Error('지원하지 않는 입력 형식입니다.'));
        }
      });
    },

    _mergeImportedData: function (data) {
      let importedDeals = [];
      if (Array.isArray(data)) {
        importedDeals = data;
      } else if (data && Array.isArray(data.deals)) {
        importedDeals = data.deals;
      } else if (data && data.id && data.property) {
        importedDeals = [data];
      } else {
        throw new Error('유효한 거래 데이터 형식이 아닙니다.');
      }

      const existingList = this.listDeals();
      const existingMap = {};
      existingList.forEach(function (d) { existingMap[d.id] = d; });

      let addedCount = 0;
      let updatedCount = 0;

      importedDeals.forEach(function (deal) {
        if (!deal.id) deal.id = 'deal_' + Date.now() + '_' + Math.random().toString(36).substring(2, 7);
        if (existingMap[deal.id]) {
          const tExisting = new Date(existingMap[deal.id].updatedAt || existingMap[deal.id].createdAt || 0).getTime();
          const tImported = new Date(deal.updatedAt || deal.createdAt || 0).getTime();
          if (tImported >= tExisting) {
            existingMap[deal.id] = deal;
            updatedCount++;
          }
        } else {
          existingMap[deal.id] = deal;
          addedCount++;
        }
      });

      const mergedList = Object.values(existingMap).sort(function (a, b) {
        const tA = new Date(a.updatedAt || a.createdAt || 0).getTime();
        const tB = new Date(b.updatedAt || b.createdAt || 0).getTime();
        return tB - tA;
      });

      localStorage.setItem(STORAGE_KEY, JSON.stringify(mergedList));
      return { total: mergedList.length, added: addedCount, updated: updatedCount };
    },

    /**
     * 표준 파일명 생성
     * 규칙: YYYYMMDD_법정동_단지명_동호수_문서구분
     */
    generateStandardFileName: function (deal, docType) {
      if (!deal) return '문서';
      let datePart = (deal.dealDate || '').replace(/-/g, '');
      if (!datePart) {
        const now = new Date();
        const y = now.getFullYear();
        const m = String(now.getMonth() + 1).padStart(2, '0');
        const d = String(now.getDate()).padStart(2, '0');
        datePart = `${y}${m}${d}`;
      }

      const prop = deal.property || {};
      const dong = (prop.dong || '').trim();
      const complex = (prop.complex || '').trim();
      const dongNum = (prop.dongNum || '').trim();
      const hoNum = (prop.hoNum || '').trim();

      let unitPart = '';
      if (dongNum && hoNum) unitPart = `${dongNum}동${hoNum}호`;
      else if (dongNum) unitPart = `${dongNum}동`;
      else if (hoNum) unitPart = `${hoNum}호`;

      const parts = [datePart, dong, complex, unitPart, docType || '문서'].filter(Boolean);
      return parts.join('_');
    },

    /**
     * 숫자 원 단위 3자리 콤마 포맷팅
     */
    formatNumber: function (num) {
      if (num === null || num === undefined || num === '' || isNaN(num)) return '0';
      return Math.round(Number(num)).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    },

    /**
     * 날짜 포맷팅: YYYY년 MM월 DD일
     */
    formatDateKorean: function (dateStr) {
      if (!dateStr) return '';
      const parts = String(dateStr).split('-');
      if (parts.length === 3) {
        return `${parts[0]}년 ${parseInt(parts[1], 10)}월 ${parseInt(parts[2], 10)}일`;
      }
      return dateStr;
    },

    /**
     * 숫자를 한글 금액 표기로 변환
     * 엑셀 NUMBERSTRING(val, 1) 완벽 대응
     * 예: 950000000 -> "구억오천만원"
     *     30000000 -> "삼천만원"
     *     1250000000 -> "일십이억오천만원"
     */
    numToKorean: function (num) {
      if (!num || isNaN(num) || Number(num) === 0) return '영원';
      const n = Math.floor(Math.abs(Number(num)));

      const units = ['', '만', '억', '조', '경'];
      const subUnits = ['', '십', '백', '천'];
      const digits = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구'];

      let result = '';
      let unitIdx = 0;
      let temp = n;

      while (temp > 0) {
        const chunk = temp % 10000;
        if (chunk > 0) {
          let chunkStr = '';
          let subTemp = chunk;
          let subIdx = 0;

          while (subTemp > 0) {
            const digit = subTemp % 10;
            if (digit > 0) {
              chunkStr = digits[digit] + subUnits[subIdx] + chunkStr;
            }
            subTemp = Math.floor(subTemp / 10);
            subIdx++;
          }
          result = chunkStr + units[unitIdx] + result;
        }
        temp = Math.floor(temp / 10000);
        unitIdx++;
      }

      return result ? result + '원' : '영원';
    }
  };

  window.DealStore = DealStore;

})(typeof window !== 'undefined' ? window : this);
