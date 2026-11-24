import re
from bs4 import BeautifulSoup

def build_full_html():
    print("Building full toji-permit/index.html...")

    # Read the prepared pages
    with open('toji-permit/build_scripts/pages_built.html', 'r', encoding='utf-8') as f:
        pages_html = f.read()

    # Read original overlay for reference CSS & JS
    with open('toji-permit/index_overlay.html', 'r', encoding='utf-8') as f:
        overlay_html = f.read()

    # Extract JS from overlay
    js_match = re.search(r'<script>(.*?)</script>', overlay_html, re.DOTALL)
    overlay_js = js_match.group(1) if js_match else ''

    full_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>토지거래계약 허가신청서 통합 작성기 | 부동산이즈두산</title>
  <!-- Hancom Official HWP Vector & Paragraph Styles -->
  <link rel="stylesheet" type="text/css" href="source_hwp_style.css">
  
  <style>
    :root {{
      --primary: #1e3a8a;
      --primary-light: #3b82f6;
      --primary-dark: #172554;
      --accent: #2563eb;
      --bg-sidebar: #f8fafc;
      --bg-app: #e2e8f0;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --border-color: #cbd5e1;
      --panel-bg: #ffffff;
      --input-bg: #ffffff;
      --chip-bg: #e2e8f0;
      --chip-text: #334155;
    }}

    [data-theme="dark"] {{
      --primary: #3b82f6;
      --primary-light: #60a5fa;
      --primary-dark: #1d4ed8;
      --accent: #38bdf8;
      --bg-sidebar: #0f172a;
      --bg-app: #020617;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --border-color: #334155;
      --panel-bg: #1e293b;
      --input-bg: #0f172a;
      --chip-bg: #334155;
      --chip-text: #e2e8f0;
    }}

    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      padding: 0;
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, 'Malgun Gothic', sans-serif;
      background: var(--bg-app);
      color: var(--text-main);
      overflow-x: hidden;
      height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    /* Header Bar */
    .app-header {{
      height: 52px;
      background: #1e293b;
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px;
      border-bottom: 1px solid #334155;
      flex-shrink: 0;
      z-index: 50;
    }}

    .header-left {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .header-title {{
      font-size: 15px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 8px;
      color: #f8fafc;
    }}

    .header-badge {{
      font-size: 11px;
      background: rgba(59, 130, 246, 0.2);
      color: #60a5fa;
      padding: 2px 8px;
      border-radius: 9999px;
      border: 1px solid rgba(59, 130, 246, 0.3);
    }}

    .header-center {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .deal-selector-wrapper {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .deal-select {{
      height: 32px;
      background: #0f172a;
      color: #e2e8f0;
      border: 1px solid #475569;
      border-radius: 6px;
      padding: 0 10px;
      font-size: 13px;
      font-weight: 500;
      min-width: 260px;
      outline: none;
    }}

    .deal-select:focus {{
      border-color: #3b82f6;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .btn {{
      height: 32px;
      padding: 0 12px;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      border: none;
      transition: all 0.15s ease;
      text-decoration: none;
    }}

    .btn-primary {{
      background: #2563eb;
      color: #ffffff;
    }}
    .btn-primary:hover {{
      background: #1d4ed8;
    }}

    .btn-success {{
      background: #059669;
      color: #ffffff;
    }}
    .btn-success:hover {{
      background: #047857;
    }}

    .btn-outline {{
      background: transparent;
      color: #cbd5e1;
      border: 1px solid #475569;
    }}
    .btn-outline:hover {{
      background: #334155;
      color: #ffffff;
    }}

    .btn-icon {{
      width: 32px;
      height: 32px;
      padding: 0;
      justify-content: center;
    }}

    /* Main Container */
    .app-main {{
      flex: 1;
      display: flex;
      overflow: hidden;
    }}

    /* Editor Sidebar */
    .editor-panel {{
      width: 440px;
      flex-shrink: 0;
      background: var(--bg-sidebar);
      border-right: 1px solid var(--border-color);
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      height: 100%;
    }}

    .editor-content {{
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    /* Preset Chips */
    .preset-box {{
      background: var(--panel-bg);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 10px 12px;
    }}

    .preset-title {{
      font-size: 11px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      margin-bottom: 6px;
      letter-spacing: 0.5px;
    }}

    .preset-chips {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }}

    .preset-chip {{
      font-size: 12px;
      padding: 4px 9px;
      border-radius: 4px;
      background: var(--chip-bg);
      color: var(--chip-text);
      cursor: pointer;
      font-weight: 500;
      border: 1px solid transparent;
      transition: all 0.15s ease;
    }}

    .preset-chip:hover {{
      border-color: var(--primary-light);
      color: var(--primary);
    }}

    /* Form Accordions / Sections */
    .form-section {{
      background: var(--panel-bg);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      overflow: hidden;
    }}

    .section-header {{
      padding: 10px 14px;
      background: rgba(0,0,0,0.02);
      border-bottom: 1px solid var(--border-color);
      font-size: 13px;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      user-select: none;
    }}

    .section-body {{
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .field-row {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .field-row.grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }}

    .field-row.grid-3 {{
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 6px;
    }}

    .field-row.grid-4 {{
      display: grid;
      grid-template-columns: 1fr 1fr 1fr 1fr;
      gap: 6px;
    }}

    .field-label {{
      font-size: 11px;
      font-weight: 600;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .field-label .sub {{
      font-weight: 400;
      color: var(--text-muted);
    }}

    .input-box {{
      width: 100%;
      height: 32px;
      background: var(--input-bg);
      border: 1px solid var(--border-color);
      border-radius: 5px;
      padding: 0 8px;
      font-size: 12.5px;
      color: var(--text-main);
      outline: none;
      transition: border-color 0.15s ease;
    }}

    .input-box:focus {{
      border-color: var(--primary-light);
    }}

    .input-box.read-calc {{
      background: rgba(0,0,0,0.03);
      font-weight: 600;
      color: var(--primary);
    }}

    /* Preview Container */
    .preview-container {{
      flex: 1;
      display: flex;
      flex-direction: column;
      background: #cbd5e1;
      overflow: hidden;
      position: relative;
    }}

    [data-theme="dark"] .preview-container {{
      background: #020617;
    }}

    /* Preview Nav Bar (Tabs & Checklist) */
    .page-nav-bar {{
      height: 44px;
      background: var(--panel-bg);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px;
      flex-shrink: 0;
      z-index: 20;
    }}

    .page-tabs {{
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    .page-tab-btn {{
      height: 28px;
      padding: 0 10px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 600;
      border: 1px solid var(--border-color);
      background: var(--chip-bg);
      color: var(--text-main);
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .page-tab-btn:hover, .page-tab-btn.active {{
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
    }}

    .print-check-group {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-main);
    }}

    .print-check-label {{
      display: flex;
      align-items: center;
      gap: 4px;
      cursor: pointer;
      user-select: none;
    }}

    .zoom-group {{
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    .zoom-btn {{
      width: 26px;
      height: 26px;
      padding: 0;
      border-radius: 4px;
      border: 1px solid var(--border-color);
      background: var(--chip-bg);
      color: var(--text-main);
      font-size: 12px;
      cursor: pointer;
    }}

    /* Preview Scroll Area */
    .preview-scroll {{
      flex: 1;
      overflow: auto;
      padding: 24px 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 24px;
    }}

    /* Sheet Wrapper */
    .sheet-wrapper {{
      transform-origin: top center;
      transition: transform 0.2s ease;
    }}

    /* HWP Page Specifics */
    .hpa {{
      background: #ffffff !important;
      position: relative !important;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
      margin-bottom: 24px !important;
      border: 1px solid #94a3b8 !important;
    }}

    .hpa.print-excluded {{
      opacity: 0.35;
      filter: grayscale(1);
    }}

    /* Interactive Permit Fields */
    .permit-field {{
      position: absolute;
      font-family: 'Malgun Gothic', '맑은 고딕', AppleSDGothicNeo-Regular, sans-serif;
      font-size: 9.5pt;
      font-weight: 700;
      color: #111827;
      display: flex;
      align-items: center;
      line-height: 1.2;
      background: transparent;
      border: none;
      outline: none;
      white-space: nowrap;
      cursor: text;
    }}

    .permit-field:focus {{
      background: rgba(59, 130, 246, 0.12);
      border-radius: 2px;
      outline: 1.5px dashed #2563eb;
    }}

    /* Toast Notification */
    .toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #1e293b;
      color: #ffffff;
      padding: 10px 18px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      box-shadow: 0 4px 14px rgba(0,0,0,0.25);
      z-index: 1000;
      display: flex;
      align-items: center;
      gap: 8px;
      opacity: 0;
      transform: translateY(10px);
      transition: all 0.25s ease;
      pointer-events: none;
    }}

    .toast.show {{
      opacity: 1;
      transform: translateY(0);
    }}

    /* Clean A4 Zero-Margin Printing */
    @page {{
      size: 210mm 297mm;
      margin: 0mm;
    }}

    @media print {{
      html, body {{
        margin: 0 !important;
        padding: 0 !important;
        background: #ffffff !important;
        height: auto !important;
        overflow: visible !important;
      }}

      .app-header,
      .editor-panel,
      .page-nav-bar,
      .toast,
      .no-print {{
        display: none !important;
      }}

      .app-main {{
        display: block !important;
        height: auto !important;
        overflow: visible !important;
      }}

      .preview-container {{
        background: transparent !important;
        overflow: visible !important;
        display: block !important;
        height: auto !important;
      }}

      .preview-scroll {{
        padding: 0 !important;
        overflow: visible !important;
        display: block !important;
      }}

      .sheet-wrapper {{
        transform: none !important;
      }}

      .hpa {{
        margin: 0 !important;
        padding: 0 !important;
        box-shadow: none !important;
        border: none !important;
        page-break-after: always !important;
        break-after: page !important;
      }}

      .hpa.print-excluded {{
        display: none !important;
      }}

      .permit-field:focus {{
        outline: none !important;
        background: transparent !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- App Header -->
  <header class="app-header">
    <div class="header-left">
      <div class="header-title">
        <span>🏛️</span>
        <span>토지거래허가신청서 통합 작성기</span>
      </div>
      <span class="header-badge">안양시 동안구 공식서식</span>
    </div>

    <div class="header-center">
      <div class="deal-selector-wrapper deal-integration-box">
        <label for="dealSelect" style="font-size:12px; color:#94a3b8; font-weight:600;">거래 건:</label>
        <select id="dealSelect" class="deal-select" onchange="loadSelectedDealIntoPermit()">
          <option value="">-- 거래를 선택하거나 새로 작성 --</option>
        </select>
      </div>
      <button type="button" class="btn btn-outline btn-icon" onclick="resetToNewDeal()" title="새 거래 작성">✨</button>
    </div>

    <div class="header-actions">
      <button type="button" class="btn btn-success" onclick="savePermitBackToDealStore()">💾 거래 저장</button>
      <button type="button" class="btn btn-primary" onclick="printWithStandardFileName()">🖨️ A4 인쇄 / PDF</button>
      <a href="../agreement/index.html" id="linkToAgreement" class="btn btn-outline">📝 매매약정서 이동</a>
      <a href="./index_overlay.html" class="btn btn-outline" style="font-size:11px; padding:0 8px;">🖼️ 오버레이</a>
      <button type="button" class="btn btn-outline btn-icon" onclick="toggleTheme()" title="테마 전환">🌓</button>
    </div>
  </header>

  <!-- App Main -->
  <main class="app-main">
    <!-- Left Sidebar Editor -->
    <aside class="editor-panel">
      <div class="editor-content">
        <!-- Preset Chips -->
        <div class="preset-box">
          <div class="preset-title">🏢 평촌 주요 단지 프리셋 (원클릭 자동 입력)</div>
          <div class="preset-chips">
            <span class="preset-chip" onclick="applyComplexPreset('목련두산2')">목련두산 2단지</span>
            <span class="preset-chip" onclick="applyComplexPreset('목련우성3')">목련우성 3단지</span>
            <span class="preset-chip" onclick="applyComplexPreset('목련우성5')">목련우성 5단지</span>
            <span class="preset-chip" onclick="applyComplexPreset('꿈마을건영')">꿈마을건영</span>
            <span class="preset-chip" onclick="applyComplexPreset('무궁화태영')">무궁화태영</span>
          </div>
        </div>

        <!-- 1. 기본 매물 정보 -->
        <div class="form-section">
          <div class="section-header" onclick="toggleSection(this)">
            <span>📍 1. 매물 기본 정보</span>
            <span>▾</span>
          </div>
          <div class="section-body">
            <div class="field-row grid-2">
              <div>
                <label class="field-label">신청일자 <span class="sub">(공백권장)</span></label>
                <input type="date" class="input-box" id="in_date" value="" oninput="syncAll()">
                <label style="display:inline-flex; align-items:center; gap:6px; font-size:11px; margin-top:4px; cursor:pointer;">
                  <input type="checkbox" id="chk_blank_date" checked onchange="syncAll();">
                  <span>수기 작성 날짜 (       년    월    일 )</span>
                </label>
              </div>
              <div>
                <label class="field-label">법정동</label>
                <input type="text" class="input-box" id="in_dong" value="호계동" oninput="calcJibunFull(); syncAll();">
              </div>
            </div>

            <div class="field-row grid-3">
              <div>
                <label class="field-label">지번 본번</label>
                <input type="text" class="input-box" id="in_jibun_main" value="1054" oninput="calcJibunFull(); syncAll();">
              </div>
              <div>
                <label class="field-label">부번</label>
                <input type="text" class="input-box" id="in_jibun_sub" value="" placeholder="없으면 공백" oninput="calcJibunFull(); syncAll();">
              </div>
              <div>
                <label class="field-label">단지명</label>
                <input type="text" class="input-box" id="in_complex" value="목련마을두산" oninput="syncAll();">
              </div>
            </div>

            <div class="field-row grid-2">
              <div>
                <label class="field-label">동·호수 (정착물 내용)</label>
                <input type="text" class="input-box" id="in_bld_unit" value="제601동 제601호" placeholder="예: 제601동 제601호" oninput="calcJibunFull(); syncAll();">
              </div>
              <div>
                <label class="field-label">도로명 주소</label>
                <input type="text" class="input-box" id="in_road_addr" value="경기도 안양시 동안구 동안로 120" oninput="syncAll();">
              </div>
            </div>

            <div class="field-row">
              <label class="field-label">전체 지번 표시 (공적장부용)</label>
              <input type="text" class="input-box" id="in_addr_full" value="경기도 안양시 동안구 호계동 1054 목련마을두산아파트 제601동 제601호" oninput="syncAll();">
            </div>

            <div class="field-row grid-2">
              <div>
                <label class="field-label">⑩ 법정 지목</label>
                <input type="text" class="input-box" id="in_jimok_legal" value="대" oninput="syncAll();">
              </div>
              <div>
                <label class="field-label">⑪ 현실 지목</label>
                <input type="text" class="input-box" id="in_jimok_actual" value="대" oninput="syncAll();">
              </div>
            </div>

            <div class="field-row grid-3">
              <div>
                <label class="field-label">1필지 총면적(㎡)</label>
                <input type="number" step="0.01" class="input-box" id="in_land_total_area" value="56123.4" oninput="calcLandShare(); syncAll();">
              </div>
              <div>
                <label class="field-label">대지권 비율 분모</label>
                <input type="text" class="input-box" id="in_land_ratio_den" value="56123.4" oninput="calcLandShare(); syncAll();">
              </div>
              <div>
                <label class="field-label">대지권 지분(㎡)</label>
                <input type="number" step="0.01" class="input-box" id="in_land_ratio_num" value="51.84" oninput="calcLandShare(); syncAll();">
              </div>
            </div>

            <div class="field-row grid-2">
              <div>
                <label class="field-label">⑫ 대지권 지분면적 표기</label>
                <input type="text" class="input-box read-calc" id="in_land_share_display" value="51.84㎡" readonly>
              </div>
              <div>
                <label class="field-label">⑬ 용도지역</label>
                <input type="text" class="input-box" id="in_yongdo_area" value="제3종일반주거지역" oninput="syncAll();">
              </div>
            </div>

            <div class="field-row grid-2">
              <div>
                <label class="field-label">⑭ 토지이용현황</label>
                <input type="text" class="input-box" id="in_land_use_status" value="아파트" oninput="syncAll();">
              </div>
              <div>
                <label class="field-label">⑮ 권리설정현황</label>
                <input type="text" class="input-box" id="in_rights_status" value="해당없음" oninput="syncAll();">
              </div>
            </div>

            <div class="field-row grid-2">
              <div>
                <label class="field-label">⑯ 종류 (주용도)</label>
                <input type="text" class="input-box" id="in_bld_type" value="공동주택" oninput="syncAll();">
              </div>
              <div>
                <label class="field-label">전유면적(㎡)</label>
                <input type="number" step="0.01" class="input-box" id="in_exclusive_area" value="101.42" oninput="syncAll();">
              </div>
            </div>

            <div class="field-row grid-3">
              <div>
                <label class="field-label">⑱ 이전 권리 종류</label>
                <input type="text" class="input-box" id="in_right_kind" value="소유권" oninput="syncAll();">
              </div>
              <div>
                <label class="field-label">⑲ 권리 내용</label>
                <input type="text" class="input-box" id="in_right_act" value="취득" oninput="syncAll();">
              </div>
              <div>
                <label class="field-label">⑳ 이전/설정 형태</label>
                <input type="text" class="input-box" id="in_transfer_type" value="유상 (매매)" oninput="syncAll();">
              </div>
            </div>
          </div>
        </div>

        <!-- 2. 매도인 정보 -->
        <div class="form-section">
          <div class="section-header" onclick="toggleSection(this)">
            <span>👤 2. 매도인 정보</span>
            <button type="button" class="btn btn-outline" style="height:22px; font-size:11px; padding:0 6px;" onclick="event.stopPropagation(); toggleSeller2();">+ 공동매도인</button>
          </div>
          <div class="section-body">
            <div class="field-row grid-2">
              <div>
                <label class="field-label">매도인 1 성명</label>
                <input type="text" class="input-box" id="in_seller_name" value="김매도" oninput="syncAll();">
              </div>
              <div>
                <label class="field-label">주민등록번호</label>
                <input type="text" class="input-box" id="in_seller_rrn" value="700101-1234567" oninput="syncAll();">
              </div>
            </div>
            <div class="field-row grid-2">
              <div>
                <label class="field-label">연락처</label>
                <input type="text" class="input-box" id="in_seller_tel" value="010-3322-1144" oninput="syncAll();">
              </div>
              <div>
                <label class="field-label">주소</label>
                <input type="text" class="input-box" id="in_seller_addr" value="경기도 안양시 동안구 동안로 120, 101동 202호" oninput="syncAll();">
              </div>
            </div>

            <!-- 공동매도인 2 -->
            <div id="seller2_group" style="display:none; border-top:1px dashed var(--border-color); padding-top:8px; margin-top:4px;">
              <div style="font-size:11px; font-weight:700; color:var(--primary); margin-bottom:4px;">👥 공동매도인 2 (2P 별지 자동반영)</div>
              <div class="field-row grid-2">
                <div>
                  <label class="field-label">성명</label>
                  <input type="text" class="input-box" id="in_seller2_name" value="" placeholder="공동매도인 성명" oninput="syncAll();">
                </div>
                <div>
                  <label class="field-label">주민등록번호</label>
                  <input type="text" class="input-box" id="in_seller2_rrn" value="" placeholder="주민번호" oninput="syncAll();">
                </div>
              </div>
              <div class="field-row grid-2">
                <div>
                  <label class="field-label">연락처</label>
                  <input type="text" class="input-box" id="in_seller2_tel" value="" placeholder="연락처" oninput="syncAll();">
                </div>
                <div>
                  <label class="field-label">주소</label>
                  <input type="text" class="input-box" id="in_seller2_addr" value="" placeholder="주소" oninput="syncAll();">
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 3. 매수인 정보 -->
        <div class="form-section">
          <div class="section-header" onclick="toggleSection(this)">
            <span>👤 3. 매수인 정보</span>
            <button type="button" class="btn btn-outline" style="height:22px; font-size:11px; padding:0 6px;" onclick="event.stopPropagation(); toggleBuyer2();">+ 공동매수인</button>
          </div>
          <div class="section-body">
            <div class="field-row grid-2">
              <div>
                <label class="field-label">매수인 1 성명</label>
                <input type="text" class="input-box" id="in_buyer_name" value="이매수" oninput="syncAll();">
              </div>
              <div>
                <label class="field-label">주민등록번호</label>
                <input type="text" class="input-box" id="in_buyer_rrn" value="820512-2345678" oninput="syncAll();">
              </div>
            </div>
            <div class="field-row grid-2">
              <div>
                <label class="field-label">연락처</label>
                <input type="text" class="input-box" id="in_buyer_tel" value="010-9988-7766" oninput="syncAll();">
              </div>
              <div>
                <label class="field-label">주소</label>
                <input type="text" class="input-box" id="in_buyer_addr" value="서울특별시 서초구 반포대로 58, 105동 1204호" oninput="syncAll();">
              </div>
            </div>

            <!-- 공동매수인 2 -->
            <div id="buyer2_group" style="display:none; border-top:1px dashed var(--border-color); padding-top:8px; margin-top:4px;">
              <div style="font-size:11px; font-weight:700; color:var(--primary); margin-bottom:4px;">👥 공동매수인 2 (2P 별지 & 4P/7P/8P 병기)</div>
              <div class="field-row grid-2">
                <div>
                  <label class="field-label">성명</label>
                  <input type="text" class="input-box" id="in_buyer2_name" value="" placeholder="공동매수인 성명" oninput="syncAll();">
                </div>
                <div>
                  <label class="field-label">주민등록번호</label>
                  <input type="text" class="input-box" id="in_buyer2_rrn" value="" placeholder="주민번호" oninput="syncAll();">
                </div>
              </div>
              <div class="field-row grid-2">
                <div>
                  <label class="field-label">연락처</label>
                  <input type="text" class="input-box" id="in_buyer2_tel" value="" placeholder="연락처" oninput="syncAll();">
                </div>
                <div>
                  <label class="field-label">주소</label>
                  <input type="text" class="input-box" id="in_buyer2_addr" value="" placeholder="주소" oninput="syncAll();">
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 4. 거래금액 & 지분안분 -->
        <div class="form-section">
          <div class="section-header" onclick="toggleSection(this)">
            <span>💰 4. 계약예정금액 및 토지·건물 안분</span>
            <span>▾</span>
          </div>
          <div class="section-body">
            <div class="field-row">
              <label class="field-label">총 매매예정금액 (원)</label>
              <input type="number" class="input-box" id="in_total_price" value="1250000000" oninput="calcPriceBreakdown(); syncAll();">
            </div>
            <div class="field-row grid-3">
              <div>
                <label class="field-label">공시지가 단가(원/㎡)</label>
                <input type="number" class="input-box" id="in_land_official_price" value="4500000" oninput="calcPriceBreakdown(); syncAll();">
              </div>
              <div>
                <label class="field-label">토지 예정금액 (안분)</label>
                <input type="text" class="input-box read-calc" id="in_land_price_display" value="233,280,000원" readonly>
              </div>
              <div>
                <label class="field-label">건물 예정금액 (안분)</label>
                <input type="text" class="input-box read-calc" id="in_bld_price_display" value="1,016,720,000원" readonly>
              </div>
            </div>
          </div>
        </div>

        <!-- 5. 토지취득자금 조달계획 (3P) -->
        <div class="form-section">
          <div class="section-header" onclick="toggleSection(this)">
            <span>🏦 5. 자금조달계획서 세부 (3P)</span>
            <span>▾</span>
          </div>
          <div class="section-body">
            <div style="font-size:11px; font-weight:700; color:var(--text-muted); margin-bottom:4px;">매수인 1 자금조달 (기본 공백, 필요시 입력)</div>
            <div class="field-row grid-2">
              <div>
                <label class="field-label">② 금융기관 예금액(원)</label>
                <input type="number" class="input-box" id="in_fund_deposit" value="" placeholder="공백(선택입력)" oninput="syncAll();">
              </div>
              <div>
                <label class="field-label">③ 주식·채권 매각(원)</label>
                <input type="number" class="input-box" id="in_fund_stocks" value="" placeholder="공백(선택입력)" oninput="syncAll();">
              </div>
            </div>
            <div class="field-row grid-2">
              <div>
                <label class="field-label">④ 증여·상속액(원)</label>
                <input type="number" class="input-box" id="in_fund_gift" value="" placeholder="공백(선택입력)" oninput="syncAll();">
              </div>
              <div>
                <label class="field-label">⑥ 부동산 처분대금(원)</label>
                <input type="number" class="input-box" id="in_fund_realestate" value="" placeholder="공백(선택입력)" oninput="syncAll();">
              </div>
            </div>
            <div class="field-row grid-2">
              <div>
                <label class="field-label">⑩ 금융기관 대출액(원)</label>
                <input type="number" class="input-box" id="in_fund_loan_bank" value="" placeholder="공백(선택입력)" oninput="syncAll();">
              </div>
              <div>
                <label class="field-label">⑪ 그 밖의 차입금(원)</label>
                <input type="number" class="input-box" id="in_fund_borrow" value="" placeholder="공백(선택입력)" oninput="syncAll();">
              </div>
            </div>

            <!-- 공동매수인 2 자금조달계획 (공동매수인 활성화시) -->
            <div id="fund_buyer2_group" style="display:none; border-top:1px dashed var(--border-color); padding-top:8px; margin-top:8px;">
              <div style="font-size:11px; font-weight:700; color:var(--primary); margin-bottom:4px;">👥 공동매수인 2 자금조달계획 (3P-2)</div>
              <div class="field-row grid-2">
                <div>
                  <label class="field-label">② 금융기관 예금액(원)</label>
                  <input type="number" class="input-box" id="in_fund2_deposit" value="" placeholder="공백(선택입력)" oninput="syncAll();">
                </div>
                <div>
                  <label class="field-label">③ 주식·채권 매각(원)</label>
                  <input type="number" class="input-box" id="in_fund2_stocks" value="" placeholder="공백(선택입력)" oninput="syncAll();">
                </div>
              </div>
              <div class="field-row grid-2">
                <div>
                  <label class="field-label">④ 증여·상속액(원)</label>
                  <input type="number" class="input-box" id="in_fund2_gift" value="" placeholder="공백(선택입력)" oninput="syncAll();">
                </div>
                <div>
                  <label class="field-label">⑥ 부동산 처분대금(원)</label>
                  <input type="number" class="input-box" id="in_fund2_realestate" value="" placeholder="공백(선택입력)" oninput="syncAll();">
                </div>
              </div>
              <div class="field-row grid-2">
                <div>
                  <label class="field-label">⑩ 금융기관 대출액(원)</label>
                  <input type="number" class="input-box" id="in_fund2_loan_bank" value="" placeholder="공백(선택입력)" oninput="syncAll();">
                </div>
                <div>
                  <label class="field-label">⑪ 그 밖의 차입금(원)</label>
                  <input type="number" class="input-box" id="in_fund2_borrow" value="" placeholder="공백(선택입력)" oninput="syncAll();">
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 선택 서식 관리 (옵션 서식) -->
        <div class="form-section">
          <div class="section-header" onclick="toggleSection(this)">
            <span>📂 서식 선택 (선택 서식 포함 여부)</span>
            <span>▾</span>
          </div>
          <div class="section-body">
            <div style="display:flex; flex-direction:column; gap:8px; font-size:12px; padding:4px 0;">
              <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
                <input type="checkbox" id="chk_enable_plan_b" onchange="togglePlanB(this.checked)">
                <span style="font-weight:600;">5P 토지이용계획서 Ⓑ 포함</span>
                <span style="color:var(--text-muted); font-size:11px;">(실거주 유예 시 작성)</span>
              </label>
              <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
                <input type="checkbox" id="chk_enable_lease_confirm" onchange="toggleLeaseConfirm(this.checked)">
                <span style="font-weight:600;">6P 주택 임대차 계약 확인서 포함</span>
                <span style="color:var(--text-muted); font-size:11px;">(묵시적 갱신 시 작성)</span>
              </label>
              <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
                <input type="checkbox" id="chk_enable_buyer2_p3" onchange="toggleBuyer2P3(this.checked)">
                <span style="font-weight:600;">3P-2 공동매수인 자금조달계획서 포함</span>
              </label>
              <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
                <input type="checkbox" id="chk_enable_buyer2_p7" onchange="toggleBuyer2P7(this.checked)">
                <span style="font-weight:600;">7P-2 공동매수인 개인정보동의서 포함</span>
              </label>
            </div>
          </div>
        </div>

        <!-- 6. 토지이용계획서 세부 (4P) -->
        <div class="form-section">
          <div class="section-header" onclick="toggleSection(this)">
            <span>📋 6. 토지이용계획서 세부 (4P)</span>
            <span>▾</span>
          </div>
          <div class="section-body">
            <div class="field-row">
              <label class="field-label">이용목적 (토지이용계획)</label>
              <input type="text" class="input-box" id="in_purpose" value="주거용 (세대원 전원 실거주 자가주택 취득)" oninput="syncAll();">
            </div>
            <div class="field-row grid-2">
              <div>
                <label class="field-label">잔금예정일</label>
                <input type="date" class="input-box" id="in_balance_date" value="2026-12-30" oninput="syncAll();">
              </div>
              <div>
                <label class="field-label">입주예정일</label>
                <input type="date" class="input-box" id="in_move_in_date" value="2026-12-30" oninput="syncAll();">
              </div>
            </div>
            <div class="field-row grid-2">
              <div>
                <label class="field-label">점유현황</label>
                <select class="input-box" id="in_occupant_type" onchange="syncAll();">
                  <option value="매도인" selected>매도인 거주</option>
                  <option value="임차인">임차인 거주</option>
                  <option value="공가">공가(공실)</option>
                </select>
              </div>
              <div>
                <label class="field-label">임차인 퇴거예정일</label>
                <input type="date" class="input-box" id="in_tenant_vacate_date" value="" placeholder="임차인 있는 경우" oninput="syncAll();">
              </div>
            </div>
          </div>
        </div>

        <!-- 7. 중개사무소 및 수임인 정보 (8P 위임장) -->
        <div class="form-section">
          <div class="section-header" onclick="toggleSection(this)">
            <span>🏢 7. 중개사무소 및 수임인 정보 (8P 위임장)</span>
            <span>▾</span>
          </div>
          <div class="section-body">
            <div class="field-row grid-2">
              <div>
                <label class="field-label">상호</label>
                <input type="text" class="input-box" id="in_agent_office" value="부동산이즈 두산공인중개사사무소" oninput="syncAll();">
              </div>
              <div>
                <label class="field-label">대표 공인중개사 (수임인)</label>
                <input type="text" class="input-box" id="in_agent_name" value="백근영" oninput="syncAll();">
              </div>
            </div>
            <div class="field-row grid-2">
              <div>
                <label class="field-label">수임인 주민등록번호(생년월일)</label>
                <input type="text" class="input-box" id="in_agent_rrn" value="" placeholder="주민번호(또는 생년월일)" oninput="syncAll();">
              </div>
              <div>
                <label class="field-label">중개업 등록번호</label>
                <input type="text" class="input-box" id="in_agent_reg" value="41173-2022-00030" oninput="syncAll();">
              </div>
            </div>
            <div class="field-row grid-2">
              <div>
                <label class="field-label">연락처</label>
                <input type="text" class="input-box" id="in_agent_tel" value="031-388-7704" oninput="syncAll();">
              </div>
              <div>
                <label class="field-label">소재지</label>
                <input type="text" class="input-box" id="in_agent_addr" value="경기도 안양시 동안구 평촌대로179번길 39, 상가 104호" oninput="syncAll();">
              </div>
            </div>
          </div>
        </div>
      </div>
    </aside>

    <!-- Right Preview Area -->
    <section class="preview-container">
      <!-- Page Navigation & Checklist Toolbar -->
      <div class="page-nav-bar">
        <div class="page-tabs">
          <button type="button" class="page-tab-btn active" onclick="scrollToPage('1')">1P 신청서</button>
          <button type="button" class="page-tab-btn" onclick="scrollToPage('2')">2P 별지</button>
          <button type="button" class="page-tab-btn" onclick="scrollToPage('3')">3P 조달계획</button>
          <button type="button" class="page-tab-btn" id="tab_btn_3_2" style="display:none;" onclick="scrollToPage('3_2')">3P-2 조달(매수인2)</button>
          <button type="button" class="page-tab-btn" onclick="scrollToPage('4')">4P 이용계획A</button>
          <button type="button" class="page-tab-btn" id="tab_btn_5" style="display:none;" onclick="scrollToPage('5')">5P 이용계획B</button>
          <button type="button" class="page-tab-btn" id="tab_btn_6" style="display:none;" onclick="scrollToPage('6')">6P 임대확인</button>
          <button type="button" class="page-tab-btn" onclick="scrollToPage('7')">7P 개인정보</button>
          <button type="button" class="page-tab-btn" id="tab_btn_7_2" style="display:none;" onclick="scrollToPage('7_2')">7P-2 개인정보(매수인2)</button>
          <button type="button" class="page-tab-btn" onclick="scrollToPage('8')">8P 위임장</button>
        </div>

        <div class="print-check-group">
          <span>인쇄 포함:</span>
          <label class="print-check-label"><input type="checkbox" id="chk_p1" checked onchange="togglePrintPage('1', this.checked)"> 1P</label>
          <label class="print-check-label"><input type="checkbox" id="chk_p2" checked onchange="togglePrintPage('2', this.checked)"> 2P</label>
          <label class="print-check-label"><input type="checkbox" id="chk_p3" checked onchange="togglePrintPage('3', this.checked)"> 3P</label>
          <label class="print-check-label" id="lbl_chk_p3_2" style="display:none;"><input type="checkbox" id="chk_p3_2" onchange="togglePrintPage('3_2', this.checked)"> 3P-2</label>
          <label class="print-check-label"><input type="checkbox" id="chk_p4" checked onchange="togglePrintPage('4', this.checked)"> 4P</label>
          <label class="print-check-label" id="lbl_chk_p5" style="display:none;"><input type="checkbox" id="chk_p5" onchange="togglePrintPage('5', this.checked)"> 5P</label>
          <label class="print-check-label" id="lbl_chk_p6" style="display:none;"><input type="checkbox" id="chk_p6" onchange="togglePrintPage('6', this.checked)"> 6P</label>
          <label class="print-check-label"><input type="checkbox" id="chk_p7" checked onchange="togglePrintPage('7', this.checked)"> 7P</label>
          <label class="print-check-label" id="lbl_chk_p7_2" style="display:none;"><input type="checkbox" id="chk_p7_2" onchange="togglePrintPage('7_2', this.checked)"> 7P-2</label>
          <label class="print-check-label"><input type="checkbox" id="chk_p8" checked onchange="togglePrintPage('8', this.checked)"> 8P</label>
        </div>

        <div class="zoom-group">
          <button type="button" class="zoom-btn" onclick="adjustZoom(-0.05)" title="축소">➖</button>
          <span id="zoomDisplay" style="font-size:11px; font-weight:700; width:40px; text-align:center;">100%</span>
          <button type="button" class="zoom-btn" onclick="adjustZoom(0.05)" title="확대">➕</button>
        </div>
      </div>

      <!-- Preview Scroll Area -->
      <div class="preview-scroll" id="previewScroll">
        <div class="sheet-wrapper" id="sheetWrapper">
          <!-- 8 Hancom Vector Pages with Injected Field Overlays -->
{pages_html}
        </div>
      </div>
    </section>
  </main>

  <!-- Toast -->
  <div class="toast" id="toast"></div>

  <!-- Shared DealStore & Application Logic -->
  <script src="../shared/deal-store.js"></script>
  <script>
    let currentDealId = null;
    let currentZoom = 1.0;

    // Presets database
    const COMPLEX_PRESETS = {{
      '목련두산2': {{
        dong: '호계동',
        jibun_main: '1054',
        complex: '목련마을두산',
        road_addr: '경기도 안양시 동안구 동안로 120',
        total_land: '56123.4',
        ratio_den: '56123.4',
        ratio_num: '51.84',
        yongdo: '제3종일반주거지역',
        bld_type: '공동주택(아파트)',
        bld_unit: '제601동 제601호',
        official_price: '4500000',
        exclusive_area: '101.42'
      }},
      '목련우성3': {{
        dong: '호계동',
        jibun_main: '1053-1',
        complex: '목련마을우성3단지',
        road_addr: '경기도 안양시 동안구 동안로 120',
        total_land: '52140.0',
        ratio_den: '52140.0',
        ratio_num: '48.20',
        yongdo: '제3종일반주거지역',
        bld_type: '공동주택(아파트)',
        bld_unit: '제302동 제504호',
        official_price: '4450000',
        exclusive_area: '84.95'
      }},
      '목련우성5': {{
        dong: '호계동',
        jibun_main: '1052',
        complex: '목련마을우성5단지',
        road_addr: '경기도 안양시 동안구 동안로 142',
        total_land: '41200.0',
        ratio_den: '41200.0',
        ratio_num: '42.15',
        yongdo: '제3종일반주거지역',
        bld_type: '공동주택(아파트)',
        bld_unit: '제501동 제702호',
        official_price: '4400000',
        exclusive_area: '74.80'
      }},
      '꿈마을건영': {{
        dong: '귀인동',
        jibun_main: '933',
        complex: '꿈마을건영',
        road_addr: '경기도 안양시 동안구 귀인로 193',
        total_land: '48900.0',
        ratio_den: '48900.0',
        ratio_num: '55.30',
        yongdo: '제3종일반주거지역',
        bld_type: '공동주택(아파트)',
        bld_unit: '제201동 제1003호',
        official_price: '4600000',
        exclusive_area: '101.90'
      }},
      '무궁화태영': {{
        dong: '호계동',
        jibun_main: '1057',
        complex: '무궁화태영',
        road_addr: '경기도 안양시 동안구 동안로 98',
        total_land: '32000.0',
        ratio_den: '32000.0',
        ratio_num: '38.50',
        yongdo: '제3종일반주거지역',
        bld_type: '공동주택(아파트)',
        bld_unit: '제101동 제402호',
        official_price: '4100000',
        exclusive_area: '59.85'
      }}
    }};

    function formatNumber(num) {{
      if (num === null || num === undefined || num === '') return '';
      const n = typeof num === 'string' ? parseFloat(num.replace(/,/g, '')) : num;
      if (isNaN(n)) return '';
      return n.toLocaleString('ko-KR');
    }}

    function formatDateKorean(dateStr) {{
      if (!dateStr) return '';
      const parts = dateStr.split('-');
      if (parts.length === 3) {{
        return `${{parts[0]}}년 ${{parseInt(parts[1], 10)}}월 ${{parseInt(parts[2], 10)}}일`;
      }}
      return dateStr;
    }}

    function calcJibunFull() {{
      const dong = (document.getElementById('in_dong')?.value || '').trim();
      const main = (document.getElementById('in_jibun_main')?.value || '').trim();
      const sub = (document.getElementById('in_jibun_sub')?.value || '').trim();
      const complex = (document.getElementById('in_complex')?.value || '').trim();
      const unit = (document.getElementById('in_bld_unit')?.value || '').trim();

      let jibunPart = main;
      if (sub) jibunPart += `-${{sub}}`;

      let full = `경기도 안양시 동안구 ${{dong}} ${{jibunPart}}`;
      if (complex) full += ` ${{complex}}`;
      if (unit) full += ` ${{unit}}`;

      const addrFullInput = document.getElementById('in_addr_full');
      if (addrFullInput && !addrFullInput.dataset.manualEdited) {{
        addrFullInput.value = full;
      }}
      return jibunPart;
    }}

    function calcLandShare() {{
      const total = parseFloat(document.getElementById('in_land_total_area')?.value) || 0;
      const den = parseFloat(document.getElementById('in_land_ratio_den')?.value) || 0;
      const num = parseFloat(document.getElementById('in_land_ratio_num')?.value) || 0;

      let share = 0;
      if (den > 0 && num > 0) {{
        share = (total > 0 && total !== den) ? (total * (num / den)) : num;
      }}
      const displayEl = document.getElementById('in_land_share_display');
      if (displayEl) {{
        displayEl.value = share > 0 ? `${{share.toFixed(2)}}㎡` : '';
      }}
    }}

    function calcPriceBreakdown() {{
      const total = parseFloat(document.getElementById('in_total_price')?.value) || 0;
      const unitPrice = parseFloat(document.getElementById('in_land_official_price')?.value) || 0;
      const landShare = parseFloat(document.getElementById('in_land_ratio_num')?.value) || 0;

      let landPrice = Math.round(unitPrice * landShare);
      if (landPrice > total) landPrice = Math.round(total * 0.2);
      const bldPrice = Math.max(0, total - landPrice);

      const landEl = document.getElementById('in_land_price_display');
      const bldEl = document.getElementById('in_bld_price_display');
      if (landEl) landEl.value = `${{formatNumber(landPrice)}}원`;
      if (bldEl) bldEl.value = `${{formatNumber(bldPrice)}}원`;
    }}

    function syncAll() {{
      const dong = (document.getElementById('in_dong')?.value || '').trim();
      const jibunDisplay = calcJibunFull();
      const addrFull = (document.getElementById('in_addr_full')?.value || '').trim();

      const sellerName = (document.getElementById('in_seller_name')?.value || '').trim();
      const sellerRrn = (document.getElementById('in_seller_rrn')?.value || '').trim();
      const sellerTel = (document.getElementById('in_seller_tel')?.value || '').trim();
      const sellerAddr = (document.getElementById('in_seller_addr')?.value || '').trim();

      const seller2Name = (document.getElementById('in_seller2_name')?.value || '').trim();
      const seller2Rrn = (document.getElementById('in_seller2_rrn')?.value || '').trim();
      const seller2Tel = (document.getElementById('in_seller2_tel')?.value || '').trim();
      const seller2Addr = (document.getElementById('in_seller2_addr')?.value || '').trim();

      const buyerName = (document.getElementById('in_buyer_name')?.value || '').trim();
      const buyerRrn = (document.getElementById('in_buyer_rrn')?.value || '').trim();
      const buyerTel = (document.getElementById('in_buyer_tel')?.value || '').trim();
      const buyerAddr = (document.getElementById('in_buyer_addr')?.value || '').trim();

      const buyer2Name = (document.getElementById('in_buyer2_name')?.value || '').trim();
      const buyer2Rrn = (document.getElementById('in_buyer2_rrn')?.value || '').trim();
      const buyer2Tel = (document.getElementById('in_buyer2_tel')?.value || '').trim();
      const buyer2Addr = (document.getElementById('in_buyer2_addr')?.value || '').trim();

      const complex = (document.getElementById('in_complex')?.value || '').trim();
      const bldUnit = (document.getElementById('in_bld_unit')?.value || '').trim();
      const bldType = (document.getElementById('in_bld_type')?.value || '').trim();
      const yongdo = (document.getElementById('in_yongdo_area')?.value || '').trim();
      const landUse = (document.getElementById('in_land_use_status')?.value || '').trim();
      const rightsStatus = (document.getElementById('in_rights_status')?.value || '').trim();

      const jimokLegal = (document.getElementById('in_jimok_legal')?.value || '').trim();
      const jimokActual = (document.getElementById('in_jimok_actual')?.value || '').trim();
      const landRatioDen = (document.getElementById('in_land_ratio_den')?.value || '').trim();
      const landRatioNum = parseFloat(document.getElementById('in_land_ratio_num')?.value) || 0;

      let landRatioHtml = '';
      if (landRatioDen && landRatioNum > 0) {{
        landRatioHtml = `<div style="font-size: 7.2pt; font-weight: 500; white-space: nowrap;">${{formatNumber(landRatioDen)}}분의</div><div style="font-size: 7.8pt; font-weight: 700; white-space: nowrap;">${{landRatioNum.toFixed(2)}}㎡</div>`;
      }} else if (landRatioNum > 0) {{
        landRatioHtml = `<div style="font-size: 8.2pt; font-weight: 700;">${{landRatioNum.toFixed(2)}}㎡</div>`;
      }}

      const totalPrice = parseFloat(document.getElementById('in_total_price')?.value) || 0;
      const landOfficial = parseFloat(document.getElementById('in_land_official_price')?.value) || 0;
      let landPrice = Math.round(landOfficial * landRatioNum);
      if (landPrice > totalPrice) landPrice = Math.round(totalPrice * 0.2);
      const bldPrice = Math.max(0, totalPrice - landPrice);

      const agentOffice = (document.getElementById('in_agent_office')?.value || '').trim();
      const agentName = (document.getElementById('in_agent_name')?.value || '').trim();
      const agentRrn = (document.getElementById('in_agent_rrn')?.value || '').trim();
      const agentReg = (document.getElementById('in_agent_reg')?.value || '').trim();
      const agentTel = (document.getElementById('in_agent_tel')?.value || '').trim();
      const agentAddr = (document.getElementById('in_agent_addr')?.value || '').trim();

      const purpose = (document.getElementById('in_purpose')?.value || '').trim();
      const balanceDate = formatDateKorean(document.getElementById('in_balance_date')?.value);
      const moveInDate = formatDateKorean(document.getElementById('in_move_in_date')?.value);
      const occupantType = (document.getElementById('in_occupant_type')?.value || '').trim();
      const tenantVacate = formatDateKorean(document.getElementById('in_tenant_vacate_date')?.value);

      // Funding fields Buyer 1
      const fundDepositVal = (document.getElementById('in_fund_deposit')?.value || '').trim();
      const fundStocksVal = (document.getElementById('in_fund_stocks')?.value || '').trim();
      const fundGiftVal = (document.getElementById('in_fund_gift')?.value || '').trim();
      const fundRealestateVal = (document.getElementById('in_fund_realestate')?.value || '').trim();
      const fundLoanVal = (document.getElementById('in_fund_loan_bank')?.value || '').trim();
      const fundBorrowVal = (document.getElementById('in_fund_borrow')?.value || '').trim();

      const fundDeposit = parseFloat(fundDepositVal) || 0;
      const fundStocks = parseFloat(fundStocksVal) || 0;
      const fundGift = parseFloat(fundGiftVal) || 0;
      const fundRealestate = parseFloat(fundRealestateVal) || 0;
      const fundLoan = parseFloat(fundLoanVal) || 0;
      const fundBorrow = parseFloat(fundBorrowVal) || 0;
      const fundTotal = fundDeposit + fundStocks + fundGift + fundRealestate + fundLoan + fundBorrow;

      // Funding fields Buyer 2
      const fund2DepositVal = (document.getElementById('in_fund2_deposit')?.value || '').trim();
      const fund2StocksVal = (document.getElementById('in_fund2_stocks')?.value || '').trim();
      const fund2GiftVal = (document.getElementById('in_fund2_gift')?.value || '').trim();
      const fund2RealestateVal = (document.getElementById('in_fund2_realestate')?.value || '').trim();
      const fund2LoanVal = (document.getElementById('in_fund2_loan_bank')?.value || '').trim();
      const fund2BorrowVal = (document.getElementById('in_fund2_borrow')?.value || '').trim();

      const fund2Deposit = parseFloat(fund2DepositVal) || 0;
      const fund2Stocks = parseFloat(fund2StocksVal) || 0;
      const fund2Gift = parseFloat(fund2GiftVal) || 0;
      const fund2Realestate = parseFloat(fund2RealestateVal) || 0;
      const fund2Loan = parseFloat(fund2LoanVal) || 0;
      const fund2Borrow = parseFloat(fund2BorrowVal) || 0;
      const fund2Total = fund2Deposit + fund2Stocks + fund2Gift + fund2Realestate + fund2Loan + fund2Borrow;

      // Auto enable 3P-2 and 7P-2 when buyer 2 exists
      const hasBuyer2 = Boolean(buyer2Name || buyer2Rrn || buyer2Tel || buyer2Addr);
      const chkBuyer2P3 = document.getElementById('chk_enable_buyer2_p3');
      if (hasBuyer2 && chkBuyer2P3 && !chkBuyer2P3.checked) {{
        chkBuyer2P3.checked = true;
        toggleBuyer2P3(true);
      }}
      const chkBuyer2P7 = document.getElementById('chk_enable_buyer2_p7');
      if (hasBuyer2 && chkBuyer2P7 && !chkBuyer2P7.checked) {{
        chkBuyer2P7.checked = true;
        toggleBuyer2P7(true);
      }}

      // Co-parties formatted strings
      const sellerNamesFmt = seller2Name ? `${{sellerName}}, ${{seller2Name}}` : sellerName;
      const sellerRrnsFmt = seller2Rrn ? `${{sellerRrn}}, ${{seller2Rrn}}` : sellerRrn;
      const sellerTelsFmt = seller2Tel ? `${{sellerTel}}, ${{seller2Tel}}` : sellerTel;

      const buyerNamesFmt = buyer2Name ? `${{buyerName}}, ${{buyer2Name}}` : buyerName;
      const buyerRrnsFmt = buyer2Rrn ? `${{buyerRrn}}, ${{buyer2Rrn}}` : buyerRrn;
      const buyerTelsFmt = buyer2Tel ? `${{buyerTel}}, ${{buyer2Tel}}` : buyerTel;

      const p4BuyerRrnsHtml = buyer2Rrn
        ? `<div style="font-size:7pt; line-height:3.5mm;">${{buyerRrn}}</div><div style="font-size:7pt; line-height:3.5mm;">${{buyer2Rrn}}</div>`
        : `<div style="font-size:8.5pt;">${{buyerRrn}}</div>`;

      const p4BuyerTelsHtml = buyer2Tel
        ? `<div style="font-size:7pt; line-height:3.5mm;">${{buyerTel}}</div><div style="font-size:7pt; line-height:3.5mm;">${{buyer2Tel}}</div>`
        : `<div style="font-size:8.5pt;">${{buyerTel}}</div>`;

      // Page 5 Co-Seller RRN & Tel (줄바꿈), 성명은 공백 구분
      const p5SellerNamesHtml = seller2Name
        ? `<div style="font-size:8pt; font-weight:bold; white-space:nowrap;"><span style="margin-right:4mm;">${{sellerName}}</span><span>${{seller2Name}}</span></div>`
        : `<div style="font-size:8.5pt; font-weight:bold;">${{sellerName}}</div>`;
      const p5SellerRrnsHtml = seller2Rrn
        ? `<div style="font-size:7.5pt; line-height:3.5mm;">${{sellerRrn}}</div><div style="font-size:7.5pt; line-height:3.5mm;">${{seller2Rrn}}</div>`
        : `<div style="font-size:8.5pt;">${{sellerRrn}}</div>`;
      const p5SellerTelsHtml = seller2Tel
        ? `<div style="font-size:7.5pt; line-height:3.5mm;">${{sellerTel}}</div><div style="font-size:7.5pt; line-height:3.5mm;">${{seller2Tel}}</div>`
        : `<div style="font-size:8.5pt;">${{sellerTel}}</div>`;
      const p5SellerAddrHtml = (seller2Addr && seller2Addr !== sellerAddr)
        ? `<div style="font-size:6.8pt; line-height:3.2mm; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${{sellerAddr}}</div><div style="font-size:6.8pt; line-height:3.2mm; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${{seller2Addr}}</div>`
        : `<div style="font-size:7.8pt; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${{sellerAddr}}</div>`;

      let sellerBirth = '';
      if (sellerRrn && sellerRrn.length >= 6) {{
        const yy = sellerRrn.substring(0, 2);
        const mm = sellerRrn.substring(2, 4);
        const dd = sellerRrn.substring(4, 6);
        const prefix = (parseInt(yy, 10) > 30) ? '19' : '20';
        sellerBirth = `${{prefix}}${{yy}}-${{mm}}-${{dd}}`;
      }}
      let seller2Birth = '';
      if (seller2Rrn && seller2Rrn.length >= 6) {{
        const yy = seller2Rrn.substring(0, 2);
        const mm = seller2Rrn.substring(2, 4);
        const dd = seller2Rrn.substring(4, 6);
        const prefix = (parseInt(yy, 10) > 30) ? '19' : '20';
        seller2Birth = `${{prefix}}${{yy}}-${{mm}}-${{dd}}`;
      }}

      // Page 6 Lessor fields
      const p6LandlordNameHtml = seller2Name
        ? `<div style="font-size:7.5pt; line-height:3.5mm;">${{sellerName}}</div><div style="font-size:7.5pt; line-height:3.5mm;">${{seller2Name}}</div>`
        : `<div style="font-size:8.5pt; font-weight:bold;">${{sellerName}}</div>`;
      const p6LandlordBirthHtml = seller2Birth
        ? `<div style="font-size:7.5pt; line-height:3.5mm;">${{sellerBirth}}</div><div style="font-size:7.5pt; line-height:3.5mm;">${{seller2Birth}}</div>`
        : `<div style="font-size:8.5pt;">${{sellerBirth}}</div>`;
      const p6LandlordAddrHtml = (seller2Addr && seller2Addr !== sellerAddr)
        ? `<div style="font-size:6.8pt; line-height:3.2mm; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${{sellerAddr}}</div><div style="font-size:6.8pt; line-height:3.2mm; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${{seller2Addr}}</div>`
        : `<div style="font-size:7.8pt; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${{sellerAddr}}</div>`;
      const p6LandlordTelHtml = seller2Tel
        ? `<div style="font-size:7.5pt; line-height:3.5mm;">${{sellerTel}}</div><div style="font-size:7.5pt; line-height:3.5mm;">${{seller2Tel}}</div>`
        : `<div style="font-size:8.5pt;">${{sellerTel}}</div>`;

      // Date: default to handwriting blank format unless explicitly unchecked
      const chkBlankDate = document.getElementById('chk_blank_date');
      const isBlankDate = chkBlankDate ? chkBlankDate.checked : true;
      const applyDateInput = (document.getElementById('in_date')?.value || document.getElementById('in_deal_date')?.value || '').trim();
      const BLANK_DATE_TEXT = '      년      월      일';
      const applyDateFmt = (!isBlankDate && applyDateInput) ? formatDateKorean(applyDateInput) : BLANK_DATE_TEXT;

      const dataMap = {{
        apply_date_fmt: applyDateFmt,
        seller_birth: sellerBirth,
        p3_submitter_name: buyerName,
        p3_submitter_rrn: buyerRrn,
        p3_submitter_addr: buyerAddr,
        p3_submitter_tel: buyerTel,

        p3_2_submitter_name: buyer2Name,
        p3_2_submitter_rrn: buyer2Rrn,
        p3_2_submitter_addr: buyer2Addr,
        p3_2_submitter_tel: buyer2Tel,

        p4_buyer_names_fmt: buyerNamesFmt,
        p4_buyer_rrns_html: p4BuyerRrnsHtml,
        p4_buyer_tels_html: p4BuyerTelsHtml,

        p5_seller_names_fmt: sellerNamesFmt,
        p5_seller_names_html: p5SellerNamesHtml,
        p5_seller_rrns_html: p5SellerRrnsHtml,
        p5_seller_tels_html: p5SellerTelsHtml,
        p5_seller_addr_html: p5SellerAddrHtml,

        p6_landlord_name_html: p6LandlordNameHtml,
        p6_landlord_birth_html: p6LandlordBirthHtml,
        p6_landlord_addr_html: p6LandlordAddrHtml,
        p6_landlord_tel_html: p6LandlordTelHtml,

        p7_buyer_name: buyerName,
        p7_buyer_rrn: buyerRrn,
        p7_buyer_tel: buyerTel,

        p7_2_buyer_name: buyer2Name,
        p7_2_buyer_rrn: buyer2Rrn,
        p7_2_buyer_tel: buyer2Tel,

        p7_buyer_names_fmt: buyerNamesFmt,
        p7_buyer_rrns_fmt: buyerRrnsFmt,
        p7_buyer_tels_fmt: buyerTelsFmt,

        p8_seller_names_fmt: sellerNamesFmt,
        p8_seller_rrns_fmt: sellerRrnsFmt,
        p8_seller_tels_fmt: sellerTelsFmt,
        p8_buyer_names_fmt: buyerNamesFmt,
        p8_buyer_rrns_fmt: buyerRrnsFmt,
        p8_buyer_tels_fmt: buyerTelsFmt,

        // Basic
        dong: dong,
        jibun_display: jibunDisplay,
        dong_jibun: `${{dong}} ${{jibunDisplay}}`,
        addr_full: addrFull,
        complex_name_parens: complex ? `(${{complex}})` : '',
        jimok_legal: jimokLegal,
        jimok_actual: jimokActual,
        land_ratio_html: landRatioHtml,
        land_share_num: landRatioNum > 0 ? `${{landRatioNum.toFixed(2)}}` : '',
        land_share_display: landRatioNum > 0 ? `${{landRatioNum.toFixed(2)}}㎡` : '',
        yongdo_area: yongdo,
        land_use_status: landUse,
        rights_status: rightsStatus,

        // Building
        bld_type: bldType,
        bld_type_short: '공동주택',
        bld_detail: bldUnit,
        bld_desc: `${{complex}} ${{bldUnit}}`,
        exclusive_area: document.getElementById('in_exclusive_area')?.value || '',
        right_kind: document.getElementById('in_right_kind')?.value || '소유권',
        right_action: document.getElementById('in_right_act')?.value || '취득',
        transfer_type: document.getElementById('in_transfer_type')?.value || '유상 (매매)',

        // Prices
        total_price_fmt: formatNumber(totalPrice),
        land_unit_fmt: formatNumber(landOfficial),
        land_price_fmt: formatNumber(landPrice),
        bld_price_fmt: formatNumber(bldPrice),

        // Parties
        seller_name: sellerName,
        seller_rrn: sellerRrn,
        seller_tel: sellerTel,
        seller_addr: sellerAddr,
        seller_addr_p8: sellerAddr,
        seller_sign_text: sellerName,

        seller2_name: seller2Name,
        seller2_rrn: seller2Rrn,
        seller2_tel: seller2Tel,
        seller2_addr: seller2Addr,
        seller2_sign_text: seller2Name,

        buyer_name: buyerName,
        buyer_name_p4: buyerName,
        buyer_rrn: buyerRrn,
        buyer_tel: buyerTel,
        buyer_addr: buyerAddr,
        buyer_addr_p4: buyerAddr,
        buyer_addr_p8: buyerAddr,
        buyer_sign_text: buyerName,

        buyer2_name: buyer2Name,
        buyer2_rrn: buyer2Rrn,
        buyer2_tel: buyer2Tel,
        buyer2_addr: buyer2Addr,
        buyer2_sign_text: buyer2Name,

        // Agent
        agent_office: agentOffice,
        agent_name: agentName,
        agent_rrn: agentRrn,
        agent_reg: agentReg,
        agent_tel: agentTel,
        agent_addr: agentAddr,
        agent_office_full: `${{agentOffice}} (${{agentAddr}})`,
        agent_sign_text: agentName,

        // Plan & Dates
        purpose: purpose,
        balance_date: balanceDate,
        move_in_date: moveInDate,
        occupant_type: occupantType,
        tenant_vacate: tenantVacate,

        // Funding Buyer 1
        fund_deposit_fmt: fundDeposit > 0 ? formatNumber(fundDeposit) : '',
        fund_stocks_fmt: fundStocks > 0 ? formatNumber(fundStocks) : '',
        fund_gift_fmt: fundGift > 0 ? formatNumber(fundGift) : '',
        fund_realestate_fmt: fundRealestate > 0 ? formatNumber(fundRealestate) : '',
        fund_loan_fmt: fundLoan > 0 ? formatNumber(fundLoan) : '',
        fund_borrow_fmt: fundBorrow > 0 ? formatNumber(fundBorrow) : '',
        fund_total_fmt: fundTotal > 0 ? formatNumber(fundTotal) : '',

        // Funding Buyer 2
        fund2_deposit_fmt: fund2Deposit > 0 ? formatNumber(fund2Deposit) : '',
        fund2_stocks_fmt: fund2Stocks > 0 ? formatNumber(fund2Stocks) : '',
        fund2_gift_fmt: fund2Gift > 0 ? formatNumber(fund2Gift) : '',
        fund2_realestate_fmt: fund2Realestate > 0 ? formatNumber(fund2Realestate) : '',
        fund2_loan_fmt: fund2Loan > 0 ? formatNumber(fund2Loan) : '',
        fund2_borrow_fmt: fund2Borrow > 0 ? formatNumber(fund2Borrow) : '',
        fund2_total_fmt: fund2Total > 0 ? formatNumber(fund2Total) : ''
      }};

      // Apply dataMap to every [data-bind] element
      document.querySelectorAll('[data-bind]').forEach(el => {{
        const key = el.getAttribute('data-bind');
        if (dataMap[key] !== undefined) {{
          if (key.includes('html')) {{
            el.innerHTML = dataMap[key];
          }} else {{
            el.textContent = dataMap[key];
          }}
        }}
      }});

      function setSignSpacing(el, name1, name2) {{
        if (!el) return;
        if (name2) {{
          el.innerHTML = `<span style="display:inline-block; margin-right:25mm;">${{name1}}</span><span>${{name2}}</span>`;
        }} else {{
          el.innerHTML = name1;
        }}
      }}

      // Page 1 signatures
      const p1SellerSign = document.getElementById('f_p1_seller_sign_names');
      setSignSpacing(p1SellerSign, sellerName, seller2Name);

      const p1BuyerSign = document.getElementById('f_p1_buyer_sign_names');
      setSignSpacing(p1BuyerSign, buyerName, buyer2Name);

      // Page 4 signature container (2줄 바꿈)
      const p4SignContainer = document.getElementById('f_p4_sign_container');
      if (p4SignContainer) {{
        if (buyer2Name) {{
          p4SignContainer.innerHTML = `
            <div style="display:flex; flex-direction:column; align-items:flex-end; line-height:1.8;">
              <div style="display:flex; align-items:center;">
                <span style="margin-right:8mm;">매수인 :</span>
                <span style="font-weight:bold; min-width:30mm; text-align:left;">${{buyerName}}</span>
                <span style="color:#666; font-size:8.5pt; margin-left:2mm;">(서명 또는 인)</span>
              </div>
              <div style="display:flex; align-items:center; margin-top:2mm;">
                <span style="margin-right:8mm; visibility:hidden;">매수인 :</span>
                <span style="font-weight:bold; min-width:30mm; text-align:left;">${{buyer2Name}}</span>
                <span style="color:#666; font-size:8.5pt; margin-left:2mm;">(서명 또는 인)</span>
              </div>
            </div>`;
        }} else {{
          p4SignContainer.innerHTML = `
            <div style="display:flex; align-items:center;">
              <span style="margin-right:8mm;">매수인 :</span>
              <span style="font-weight:bold; min-width:35mm; text-align:left;">${{buyerName}}</span>
              <span style="color:#666; font-size:8.5pt; margin-left:2mm;">(서명 또는 인)</span>
            </div>`;
        }}
      }}
      const p4BuyerSign = document.getElementById('f_p4_sign_names');
      if (p4BuyerSign) p4BuyerSign.textContent = buyer2Name ? `${{buyerName}}   ${{buyer2Name}}` : buyerName;

      // Page 5 signatures
      const p5SellerSign = document.getElementById('f_p5_sign_seller_names');
      setSignSpacing(p5SellerSign, sellerName, seller2Name);

      const p5BuyerSign = document.getElementById('f_p5_sign_buyer_names');
      setSignSpacing(p5BuyerSign, buyerName, buyer2Name);

      // Page 6 signature container (임대인 및 임차인 통합 깔끔한 정렬)
      const p6SignContainer = document.getElementById('f_p6_sign_container');
      const p6Recipient = document.getElementById('f_p6_recipient');
      if (p6SignContainer) {{
        if (seller2Name) {{
          p6SignContainer.innerHTML = `
            <div style="display:flex; flex-direction:column; align-items:flex-end; width:100%; padding-right:15mm; font-size:9.5pt; font-family:'Malgun Gothic', sans-serif;">
              <!-- 1행: 주 임대인 -->
              <div style="display:flex; align-items:center; height:6.2mm;">
                <span style="display:inline-block; width:16mm; text-align:right; margin-right:6mm; color:#111;">임대인 :</span>
                <span style="font-weight:bold; min-width:32mm; text-align:left; color:#111;">${{sellerName}}</span>
                <span style="color:#666; font-size:8.5pt; margin-left:4mm;">(서명 또는 인)</span>
              </div>
              <!-- 2행: 공동 임대인 -->
              <div style="display:flex; align-items:center; height:6.2mm;">
                <span style="display:inline-block; width:16mm; text-align:right; margin-right:6mm; visibility:hidden;">임대인 :</span>
                <span style="font-weight:bold; min-width:32mm; text-align:left; color:#111;">${{seller2Name}}</span>
                <span style="color:#666; font-size:8.5pt; margin-left:4mm; visibility:hidden;">(서명 또는 인)</span>
              </div>
              <!-- 3행: 임차인 -->
              <div style="display:flex; align-items:center; height:6.2mm; margin-top:2mm;">
                <span style="display:inline-block; width:16mm; text-align:right; margin-right:6mm; color:#111;">임차인 :</span>
                <span style="display:inline-block; min-width:32mm; text-align:left;"></span>
                <span style="color:#666; font-size:8.5pt; margin-left:4mm;">(서명 또는 인)</span>
              </div>
            </div>`;
          if (p6Recipient) p6Recipient.style.top = '239mm';
        }} else {{
          p6SignContainer.innerHTML = `
            <div style="display:flex; flex-direction:column; align-items:flex-end; width:100%; padding-right:15mm; font-size:9.5pt; font-family:'Malgun Gothic', sans-serif;">
              <!-- 1행: 주 임대인 -->
              <div style="display:flex; align-items:center; height:6.5mm;">
                <span style="display:inline-block; width:16mm; text-align:right; margin-right:6mm; color:#111;">임대인 :</span>
                <span style="font-weight:bold; min-width:32mm; text-align:left; color:#111;">${{sellerName}}</span>
                <span style="color:#666; font-size:8.5pt; margin-left:4mm;">(서명 또는 인)</span>
              </div>
              <!-- 2행: 임차인 -->
              <div style="display:flex; align-items:center; height:6.5mm; margin-top:3mm;">
                <span style="display:inline-block; width:16mm; text-align:right; margin-right:6mm; color:#111;">임차인 :</span>
                <span style="display:inline-block; min-width:32mm; text-align:left;"></span>
                <span style="color:#666; font-size:8.5pt; margin-left:4mm;">(서명 또는 인)</span>
              </div>
            </div>`;
          if (p6Recipient) p6Recipient.style.top = '235mm';
        }}
      }}
      const p6LandlordSign = document.getElementById('f_p6_sign_landlord_names');
      if (p6LandlordSign) p6LandlordSign.textContent = seller2Name ? `${{sellerName}}   ${{seller2Name}}` : sellerName;

      // Page 8 signatures
      const p8SellerSign = document.getElementById('f_p8_sign_seller_names');
      setSignSpacing(p8SellerSign, sellerName, seller2Name);

      const p8BuyerSign = document.getElementById('f_p8_sign_buyer_names');
      setSignSpacing(p8BuyerSign, buyerName, buyer2Name);
    }}

    function applyComplexPreset(key) {{
      const p = COMPLEX_PRESETS[key];
      if (!p) return;
      document.getElementById('in_dong').value = p.dong;
      document.getElementById('in_jibun_main').value = p.jibun_main;
      document.getElementById('in_complex').value = p.complex;
      document.getElementById('in_road_addr').value = p.road_addr;
      document.getElementById('in_land_total_area').value = p.total_land;
      document.getElementById('in_land_ratio_den').value = p.ratio_den;
      document.getElementById('in_land_ratio_num').value = p.ratio_num;
      document.getElementById('in_yongdo_area').value = p.yongdo;
      document.getElementById('in_bld_type').value = p.bld_type;
      document.getElementById('in_bld_unit').value = p.bld_unit;
      document.getElementById('in_land_official_price').value = p.official_price;
      document.getElementById('in_exclusive_area').value = p.exclusive_area;

      calcJibunFull();
      calcLandShare();
      calcPriceBreakdown();
      syncAll();
      showToast(`🏢 '${{p.complex}}' 프리셋이 적용되었습니다.`);
    }}

    function toggleSeller2() {{
      const grp = document.getElementById('seller2_group');
      if (grp.style.display === 'none') {{
        grp.style.display = 'block';
        showToast('👥 공동매도인 2 입력란이 활성화되었습니다.');
      }} else {{
        grp.style.display = 'none';
        document.getElementById('in_seller2_name').value = '';
        document.getElementById('in_seller2_rrn').value = '';
        document.getElementById('in_seller2_tel').value = '';
        document.getElementById('in_seller2_addr').value = '';
        syncAll();
      }}
    }}

    function toggleBuyer2() {{
      const grp = document.getElementById('buyer2_group');
      const isCurrentlyHidden = (grp.style.display === 'none');
      if (isCurrentlyHidden) {{
        grp.style.display = 'block';
        const chk3 = document.getElementById('chk_enable_buyer2_p3');
        if (chk3 && !chk3.checked) {{
          chk3.checked = true;
          toggleBuyer2P3(true);
        }}
        const chk7 = document.getElementById('chk_enable_buyer2_p7');
        if (chk7 && !chk7.checked) {{
          chk7.checked = true;
          toggleBuyer2P7(true);
        }}
        showToast('👥 공동매수인 2 입력란 및 서식이 활성화되었습니다.');
      }} else {{
        grp.style.display = 'none';
        const b2Name = (document.getElementById('in_buyer2_name')?.value || '').trim();
        if (!b2Name) {{
          const chk3 = document.getElementById('chk_enable_buyer2_p3');
          if (chk3 && chk3.checked) {{
            chk3.checked = false;
            toggleBuyer2P3(false);
          }}
          const chk7 = document.getElementById('chk_enable_buyer2_p7');
          if (chk7 && chk7.checked) {{
            chk7.checked = false;
            toggleBuyer2P7(false);
          }}
        }}
        syncAll();
      }}
    }}

    function togglePlanB(isChecked) {{
      const p5 = document.getElementById('page_5');
      if (p5) {{
        p5.style.display = isChecked ? 'block' : 'none';
        p5.classList.toggle('print-excluded', !isChecked);
      }}
      const tab = document.getElementById('tab_btn_5');
      if (tab) tab.style.display = isChecked ? 'inline-block' : 'none';
      const chk = document.getElementById('chk_p5');
      if (chk) chk.checked = isChecked;
      const lbl = document.getElementById('lbl_chk_p5');
      if (lbl) lbl.style.display = isChecked ? 'inline-flex' : 'none';
    }}

    function toggleLeaseConfirm(isChecked) {{
      const p6 = document.getElementById('page_6');
      if (p6) {{
        p6.style.display = isChecked ? 'block' : 'none';
        p6.classList.toggle('print-excluded', !isChecked);
      }}
      const tab = document.getElementById('tab_btn_6');
      if (tab) tab.style.display = isChecked ? 'inline-block' : 'none';
      const chk = document.getElementById('chk_p6');
      if (chk) chk.checked = isChecked;
      const lbl = document.getElementById('lbl_chk_p6');
      if (lbl) lbl.style.display = isChecked ? 'inline-flex' : 'none';
    }}

    function toggleBuyer2P3(isChecked) {{
      const p3_2 = document.getElementById('page_3_2');
      if (p3_2) {{
        p3_2.style.display = isChecked ? 'block' : 'none';
        p3_2.classList.toggle('print-excluded', !isChecked);
      }}
      const tab = document.getElementById('tab_btn_3_2');
      if (tab) tab.style.display = isChecked ? 'inline-block' : 'none';
      const chk = document.getElementById('chk_p3_2');
      if (chk) chk.checked = isChecked;
      const lbl = document.getElementById('lbl_chk_p3_2');
      if (lbl) lbl.style.display = isChecked ? 'inline-flex' : 'none';
      const fundGrp = document.getElementById('fund_buyer2_group');
      if (fundGrp) fundGrp.style.display = isChecked ? 'block' : 'none';
      const optChk = document.getElementById('chk_enable_buyer2_p3');
      if (optChk && optChk.checked !== isChecked) optChk.checked = isChecked;
    }}

    function toggleBuyer2P7(isChecked) {{
      const p7_2 = document.getElementById('page_7_2');
      if (p7_2) {{
        p7_2.style.display = isChecked ? 'block' : 'none';
        p7_2.classList.toggle('print-excluded', !isChecked);
      }}
      const tab = document.getElementById('tab_btn_7_2');
      if (tab) tab.style.display = isChecked ? 'inline-block' : 'none';
      const chk = document.getElementById('chk_p7_2');
      if (chk) chk.checked = isChecked;
      const lbl = document.getElementById('lbl_chk_p7_2');
      if (lbl) lbl.style.display = isChecked ? 'inline-flex' : 'none';
      const optChk = document.getElementById('chk_enable_buyer2_p7');
      if (optChk && optChk.checked !== isChecked) optChk.checked = isChecked;
    }}

    function toggleSection(headerEl) {{
      const body = headerEl.nextElementSibling;
      const arrow = headerEl.querySelector('span:last-child');
      if (body.style.display === 'none') {{
        body.style.display = 'flex';
        if (arrow) arrow.textContent = '▾';
      }} else {{
        body.style.display = 'none';
        if (arrow) arrow.textContent = '▸';
      }}
    }}

    function scrollToPage(pNum) {{
      const pEl = document.getElementById(`page_${{pNum}}`);
      if (pEl) {{
        pEl.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
        document.querySelectorAll('.page-tab-btn').forEach((btn) => {{
          btn.classList.remove('active');
        }});
        const activeBtn = document.querySelector(`.page-tab-btn[onclick*="'${{pNum}}'"]`);
        if (activeBtn) activeBtn.classList.add('active');
      }}
    }}

    function togglePrintPage(pNum, isChecked) {{
      const pEl = document.getElementById(`page_${{pNum}}`);
      if (pEl) {{
        pEl.classList.toggle('print-excluded', !isChecked);
      }}
    }}

    function adjustZoom(delta) {{
      currentZoom = Math.max(0.5, Math.min(1.5, currentZoom + delta));
      const wrapper = document.getElementById('sheetWrapper');
      if (wrapper) {{
        wrapper.style.transform = `scale(${{currentZoom}})`;
      }}
      const disp = document.getElementById('zoomDisplay');
      if (disp) {{
        disp.textContent = `${{Math.round(currentZoom * 100)}}%`;
      }}
    }}

    function toggleTheme() {{
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('realty_theme', next);
    }}

    function showToast(msg) {{
      const t = document.getElementById('toast');
      if (!t) return;
      t.textContent = msg;
      t.classList.add('show');
      setTimeout(() => {{
        t.classList.remove('show');
      }}, 2600);
    }}

    // DealStore Integration
    function initPermitDealDropdown() {{
      if (typeof DealStore === 'undefined') return;
      const select = document.getElementById('dealSelect');
      if (!select) return;

      const deals = DealStore.listDeals();
      select.innerHTML = '<option value="">-- 거래를 선택하거나 새로 작성 --</option>';
      deals.forEach(d => {{
        const opt = document.createElement('option');
        opt.value = d.id;
        opt.textContent = `${{d.title || d.id}} (${{formatNumber(d.totalPrice)}}원)`;
        select.appendChild(opt);
      }});

      // Check URL dealId parameter
      const params = new URLSearchParams(window.location.search);
      const urlDealId = params.get('dealId');
      if (urlDealId && DealStore.getDeal(urlDealId)) {{
        select.value = urlDealId;
        currentDealId = urlDealId;
        loadSelectedDealIntoPermit();
      }} else if (deals.length > 0 && !currentDealId) {{
        select.value = deals[0].id;
        currentDealId = deals[0].id;
        loadSelectedDealIntoPermit();
      }}
    }}

    function applyDealToInputs(deal) {{
      if (!deal) return;
      currentDealId = deal.id;

      const p = deal.property || {{}};
      // 엑셀 서식 주소 파싱 보조
      if (!p.dong && (p.landAddr || p.bldAddr)) {{
        const full = p.landAddr || p.bldAddr;
        const mDong = full.match(/([가-힣\d]+동)\s+(\d+(?:-\d+)?)/);
        if (mDong) {{
          p.dong = mDong[1];
          const parts = mDong[2].split('-');
          p.jibunMain = parts[0];
          p.jibunSub = parts[1] || '';
        }}
      }}

      if (deal.dealDate) document.getElementById('in_date').value = deal.dealDate;
      if (deal.dong) document.getElementById('in_dong').value = deal.dong;
      if (deal.jibunMain) document.getElementById('in_jibun_main').value = deal.jibunMain;
      if (deal.jibunSub) document.getElementById('in_jibun_sub').value = deal.jibunSub;
      if (deal.complex) document.getElementById('in_complex').value = deal.complex;
      if (deal.unit) document.getElementById('in_bld_unit').value = deal.unit;
      if (deal.addrRoad) document.getElementById('in_road_addr').value = deal.addrRoad;
      if (deal.addrFull) document.getElementById('in_addr_full').value = deal.addrFull;

      if (deal.landCategory) document.getElementById('in_jimok_legal').value = deal.landCategory;
      if (deal.landArea) document.getElementById('in_land_total_area').value = deal.landArea;
      if (deal.landRatioDen) document.getElementById('in_land_ratio_den').value = deal.landRatioDen;
      if (deal.landRatioNum) document.getElementById('in_land_ratio_num').value = deal.landRatioNum;
      if (deal.buildingArea) document.getElementById('in_exclusive_area').value = deal.buildingArea;
      if (deal.zoning) document.getElementById('in_yongdo_area').value = deal.zoning;

      // Seller
      const sellersList = (deal.sellers && deal.sellers.length > 0) ? deal.sellers : ((deal.parties && deal.parties.sellers) || []);
      if (sellersList.length > 0) {{
        const s1 = sellersList[0];
        document.getElementById('in_seller_name').value = s1.name || '';
        document.getElementById('in_seller_rrn').value = s1.rrn || '';
        document.getElementById('in_seller_tel').value = s1.tel || '';
        document.getElementById('in_seller_addr').value = s1.addr || '';

        if (sellersList.length > 1) {{
          const s2 = sellersList[1];
          document.getElementById('in_seller2_name').value = s2.name || '';
          document.getElementById('in_seller2_rrn').value = s2.rrn || '';
          document.getElementById('in_seller2_tel').value = s2.tel || '';
          document.getElementById('in_seller2_addr').value = s2.addr || '';
          document.getElementById('seller2_group').style.display = 'block';
        }} else {{
          document.getElementById('seller2_group').style.display = 'none';
        }}
      }}

      // Buyer
      const buyersList = (deal.buyers && deal.buyers.length > 0) ? deal.buyers : ((deal.parties && deal.parties.buyers) || []);
      if (buyersList.length > 0) {{
        const b1 = buyersList[0];
        document.getElementById('in_buyer_name').value = b1.name || '';
        document.getElementById('in_buyer_rrn').value = b1.rrn || '';
        document.getElementById('in_buyer_tel').value = b1.tel || '';
        document.getElementById('in_buyer_addr').value = b1.addr || '';

        if (buyersList.length > 1) {{
          const b2 = buyersList[1];
          document.getElementById('in_buyer2_name').value = b2.name || '';
          document.getElementById('in_buyer2_rrn').value = b2.rrn || '';
          document.getElementById('in_buyer2_tel').value = b2.tel || '';
          document.getElementById('in_buyer2_addr').value = b2.addr || '';
          document.getElementById('buyer2_group').style.display = 'block';

          // Automatically enable 3P-2 and 7P-2
          const chk3 = document.getElementById('chk_enable_buyer2_p3');
          if (chk3) {{ chk3.checked = true; toggleBuyer2P3(true); }}
          const chk7 = document.getElementById('chk_enable_buyer2_p7');
          if (chk7) {{ chk7.checked = true; toggleBuyer2P7(true); }}
        }} else {{
          document.getElementById('buyer2_group').style.display = 'none';
        }}
      }}

      // Price
      if (deal.totalPrice) {{
        document.getElementById('in_total_price').value = deal.totalPrice;
      }}
      if (deal.balanceDate) {{
        document.getElementById('in_balance_date').value = deal.balanceDate;
      }}

      // Funding
      if (deal.funding) {{
        if (deal.funding.deposit) document.getElementById('in_fund_deposit').value = deal.funding.deposit;
        if (deal.funding.stocks) document.getElementById('in_fund_stocks').value = deal.funding.stocks;
        if (deal.funding.gift) document.getElementById('in_fund_gift').value = deal.funding.gift;
        if (deal.funding.realestate) document.getElementById('in_fund_realestate').value = deal.funding.realestate;
        if (deal.funding.loanBank) document.getElementById('in_fund_loan_bank').value = deal.funding.loanBank;
        if (deal.funding.borrow) document.getElementById('in_fund_borrow').value = deal.funding.borrow;
      }}

      // Usage Plan
      if (deal.usagePlan) {{
        if (deal.usagePlan.purpose) document.getElementById('in_purpose').value = deal.usagePlan.purpose;
        if (deal.usagePlan.moveInDate) document.getElementById('in_move_in_date').value = deal.usagePlan.moveInDate;
        if (deal.usagePlan.occupantType) document.getElementById('in_occupant_type').value = deal.usagePlan.occupantType;
        if (deal.usagePlan.tenantVacate) document.getElementById('in_tenant_vacate_date').value = deal.usagePlan.tenantVacate;
      }}

      // Update agreement link
      const linkEl = document.getElementById('linkToAgreement');
      if (linkEl) {{
        linkEl.href = `../agreement/index.html?dealId=${{deal.id}}`;
      }}

      calcJibunFull();
      calcLandShare();
      calcPriceBreakdown();
      syncAll();
    }}

    function loadSelectedDealIntoPermit() {{
      const select = document.getElementById('dealSelect');
      const dealId = select.value;
      if (!dealId || typeof DealStore === 'undefined') return;

      const deal = DealStore.getDeal(dealId);
      if (deal) {{
        applyDealToInputs(deal);
        showToast(`📂 '${{deal.title}}' 거래 데이터를 불러왔습니다.`);
      }}
    }}

    function savePermitBackToDealStore() {{
      if (typeof DealStore === 'undefined') return;

      let deal = currentDealId ? (DealStore.getDeal(currentDealId) || DealStore.createEmptyDeal()) : DealStore.createEmptyDeal();

      deal.dealDate = document.getElementById('in_date').value || deal.dealDate;
      deal.dong = document.getElementById('in_dong').value;
      deal.jibunMain = document.getElementById('in_jibun_main').value;
      deal.jibunSub = document.getElementById('in_jibun_sub').value;
      deal.complex = document.getElementById('in_complex').value;
      deal.unit = document.getElementById('in_bld_unit').value;
      deal.addrRoad = document.getElementById('in_road_addr').value;
      deal.addrFull = document.getElementById('in_addr_full').value;

      deal.landCategory = document.getElementById('in_jimok_legal').value;
      deal.landArea = parseFloat(document.getElementById('in_land_total_area').value) || 0;
      deal.landRatioDen = document.getElementById('in_land_ratio_den').value;
      deal.landRatioNum = parseFloat(document.getElementById('in_land_ratio_num').value) || 0;
      deal.buildingArea = parseFloat(document.getElementById('in_exclusive_area').value) || 0;
      deal.zoning = document.getElementById('in_yongdo_area').value;

      // Sellers
      const s2Name = document.getElementById('in_seller2_name').value.trim();
      const sellers = [{{
        name: document.getElementById('in_seller_name').value.trim(),
        rrn: document.getElementById('in_seller_rrn').value.trim(),
        tel: document.getElementById('in_seller_tel').value.trim(),
        addr: document.getElementById('in_seller_addr').value.trim(),
        share: s2Name ? '1/2' : '1/1'
      }}];
      if (s2Name) {{
        sellers.push({{
          name: s2Name,
          rrn: document.getElementById('in_seller2_rrn').value.trim(),
          tel: document.getElementById('in_seller2_tel').value.trim(),
          addr: document.getElementById('in_seller2_addr').value.trim(),
          share: '1/2'
        }});
      }}
      deal.sellers = sellers;
      deal.parties = deal.parties || {{}};
      deal.parties.sellers = sellers;

      // Buyers
      const b2Name = document.getElementById('in_buyer2_name').value.trim();
      const buyers = [{{
        name: document.getElementById('in_buyer_name').value.trim(),
        rrn: document.getElementById('in_buyer_rrn').value.trim(),
        tel: document.getElementById('in_buyer_tel').value.trim(),
        addr: document.getElementById('in_buyer_addr').value.trim(),
        share: b2Name ? '1/2' : '1/1'
      }}];
      if (b2Name) {{
        buyers.push({{
          name: b2Name,
          rrn: document.getElementById('in_buyer2_rrn').value.trim(),
          tel: document.getElementById('in_buyer2_tel').value.trim(),
          addr: document.getElementById('in_buyer2_addr').value.trim(),
          share: '1/2'
        }});
      }}
      deal.buyers = buyers;
      deal.parties = deal.parties || {{}};
      deal.parties.buyers = buyers;

      deal.totalPrice = parseFloat(document.getElementById('in_total_price').value) || 0;
      deal.balanceDate = document.getElementById('in_balance_date').value;

      // Funding
      deal.funding = {{
        deposit: parseFloat(document.getElementById('in_fund_deposit').value) || 0,
        stocks: parseFloat(document.getElementById('in_fund_stocks').value) || 0,
        gift: parseFloat(document.getElementById('in_fund_gift').value) || 0,
        realestate: parseFloat(document.getElementById('in_fund_realestate').value) || 0,
        loanBank: parseFloat(document.getElementById('in_fund_loan_bank').value) || 0,
        borrow: parseFloat(document.getElementById('in_fund_borrow').value) || 0
      }};

      // Usage Plan
      deal.usagePlan = {{
        purpose: document.getElementById('in_purpose').value.trim(),
        balanceDate: document.getElementById('in_balance_date').value,
        moveInDate: document.getElementById('in_move_in_date').value,
        occupantType: document.getElementById('in_occupant_type').value,
        tenantVacate: document.getElementById('in_tenant_vacate_date').value
      }};

      const saved = DealStore.saveDeal(deal);
      currentDealId = saved.id;
      initPermitDealDropdown();
      document.getElementById('dealSelect').value = saved.id;
      showToast(`💾 '${{saved.title}}' 거래가 저장되었습니다.`);
    }}

    function resetToNewDeal() {{
      if (typeof DealStore === 'undefined') return;
      const empty = DealStore.createEmptyDeal();
      currentDealId = empty.id;
      document.getElementById('dealSelect').value = '';
      applyDealToInputs(empty);
      showToast('✨ 새로운 거래 작성을 시작합니다.');
    }}

    function printWithStandardFileName() {{
      let fileName = '토지거래허가신청서';
      if (typeof DealStore !== 'undefined' && currentDealId) {{
        const deal = DealStore.getDeal(currentDealId);
        if (deal) {{
          fileName = DealStore.generateStandardFileName(deal, 'permit');
        }}
      }}
      const oldTitle = document.title;
      document.title = fileName;
      window.print();
      setTimeout(() => {{
        document.title = oldTitle;
      }}, 1000);
    }}

    // Two-way inline editing on sheet
    function initInlineSync() {{
      document.querySelectorAll('.permit-field[contenteditable="true"]').forEach(el => {{
        el.addEventListener('input', () => {{
          const bindKey = el.getAttribute('data-bind');
          // Find matching input in sidebar
          const mapping = {{
            'seller_name': 'in_seller_name',
            'seller_rrn': 'in_seller_rrn',
            'seller_tel': 'in_seller_tel',
            'seller_addr': 'in_seller_addr',
            'seller2_name': 'in_seller2_name',
            'seller2_rrn': 'in_seller2_rrn',
            'seller2_tel': 'in_seller2_tel',
            'seller2_addr': 'in_seller2_addr',
            'buyer_name': 'in_buyer_name',
            'buyer_rrn': 'in_buyer_rrn',
            'buyer_tel': 'in_buyer_tel',
            'buyer_addr': 'in_buyer_addr',
            'buyer2_name': 'in_buyer2_name',
            'buyer2_rrn': 'in_buyer2_rrn',
            'buyer2_tel': 'in_buyer2_tel',
            'buyer2_addr': 'in_buyer2_addr',
            'bld_detail': 'in_bld_unit',
            'purpose': 'in_purpose'
          }};
          const targetId = mapping[bindKey];
          if (targetId) {{
            const input = document.getElementById(targetId);
            if (input) {{
              input.value = el.textContent.trim();
              syncAll();
            }}
          }}
        }});
      }});
    }}

    // Initialization
    window.addEventListener('DOMContentLoaded', () => {{
      const savedTheme = localStorage.getItem('realty_theme') || 'light';
      document.documentElement.setAttribute('data-theme', savedTheme);

      calcJibunFull();
      calcLandShare();
      calcPriceBreakdown();
      syncAll();

      initPermitDealDropdown();
      initInlineSync();
    }});
  </script>
</body>
</html>
"""

    with open('toji-permit/index.html', 'w', encoding='utf-8') as out:
        out.write(full_html)

    print(f"toji-permit/index.html built successfully! (Size: {len(full_html)} bytes)")

if __name__ == '__main__':
    build_full_html()
