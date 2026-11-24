import re
import copy
from bs4 import BeautifulSoup

def build_permit():
    print("Reading source_hwp.html...")
    with open('toji-permit/source_hwp.html', 'r', encoding='utf-8') as f:
        hwp_html = f.read()

    soup = BeautifulSoup(hwp_html, 'html.parser')
    pages = soup.find_all('div', class_='hpa')
    assert len(pages) == 8, f"Expected 8 pages, found {len(pages)}"

    # =========================================================================
    # 1. PAGE 1 (토지거래계약 허가 신청서)
    # =========================================================================
    p1 = pages[0]
    hce1 = p1.find_all('div', class_='hce')

    # Parties
    hce1[10].append(soup.new_tag('div', attrs={
        'id': 'f_p1_seller_name', 'class': 'permit-cell-val', 'data-bind': 'seller_name',
        'style': 'position:absolute; left:25mm; top:0; width:calc(100% - 26mm); height:100%; display:flex; align-items:center; font-size:8.5pt; font-weight:bold;',
        'contenteditable': 'true'
    }))
    hce1[11].append(soup.new_tag('div', attrs={
        'id': 'f_p1_seller_rrn', 'class': 'permit-cell-val', 'data-bind': 'seller_rrn',
        'style': 'position:absolute; left:0; bottom:0.8mm; width:100%; height:4.2mm; display:flex; align-items:center; justify-content:center; font-size:8.5pt;',
        'contenteditable': 'true'
    }))
    hce1[12].append(soup.new_tag('div', attrs={
        'id': 'f_p1_seller_addr', 'class': 'permit-cell-val', 'data-bind': 'seller_addr',
        'style': 'position:absolute; left:1mm; bottom:0.8mm; width:calc(100% - 2mm); height:4.2mm; display:flex; align-items:center; font-size:7.5pt; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;',
        'contenteditable': 'true'
    }))
    hce1[13].append(soup.new_tag('div', attrs={
        'id': 'f_p1_seller_tel', 'class': 'permit-cell-val', 'data-bind': 'seller_tel',
        'style': 'position:absolute; left:0; bottom:0.8mm; width:100%; height:4.2mm; display:flex; align-items:center; justify-content:center; font-size:8.5pt;',
        'contenteditable': 'true'
    }))

    hce1[15].append(soup.new_tag('div', attrs={
        'id': 'f_p1_buyer_name', 'class': 'permit-cell-val', 'data-bind': 'buyer_name',
        'style': 'position:absolute; left:25mm; top:0; width:calc(100% - 26mm); height:100%; display:flex; align-items:center; font-size:8.5pt; font-weight:bold;',
        'contenteditable': 'true'
    }))
    hce1[16].append(soup.new_tag('div', attrs={
        'id': 'f_p1_buyer_rrn', 'class': 'permit-cell-val', 'data-bind': 'buyer_rrn',
        'style': 'position:absolute; left:0; bottom:0.8mm; width:100%; height:4.2mm; display:flex; align-items:center; justify-content:center; font-size:8.5pt;',
        'contenteditable': 'true'
    }))
    hce1[17].append(soup.new_tag('div', attrs={
        'id': 'f_p1_buyer_addr', 'class': 'permit-cell-val', 'data-bind': 'buyer_addr',
        'style': 'position:absolute; left:1mm; bottom:0.8mm; width:calc(100% - 2mm); height:4.2mm; display:flex; align-items:center; font-size:7.5pt; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;',
        'contenteditable': 'true'
    }))
    hce1[18].append(soup.new_tag('div', attrs={
        'id': 'f_p1_buyer_tel', 'class': 'permit-cell-val', 'data-bind': 'buyer_tel',
        'style': 'position:absolute; left:0; bottom:0.8mm; width:100%; height:4.2mm; display:flex; align-items:center; justify-content:center; font-size:8.5pt;',
        'contenteditable': 'true'
    }))

    # Right kind checkbox
    hce1[21].clear()
    hce1[21].append(BeautifulSoup('<div style="width:100%; height:100%; display:flex; align-items:center; padding-left:5mm; font-size:8.5pt;"><span style="color:#1e3a8a; font-weight:bold; margin-right:8mm;">[✔] 소유권</span><span>[ ] 지상권</span></div>', 'html.parser'))

    # Land
    hce1[33].clear()
    hce1[33].append(BeautifulSoup('<div id="f_p1_dong" class="permit-cell-val" data-bind="dong" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))
    hce1[34].clear()
    hce1[34].append(BeautifulSoup('<div id="f_p1_jibun" class="permit-cell-val" data-bind="jibun_display" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))
    hce1[35].clear()
    hce1[35].append(BeautifulSoup('<div id="f_p1_jimok_legal" class="permit-cell-val" data-bind="jimok_legal" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt;" contenteditable="true"></div>', 'html.parser'))
    hce1[36].clear()
    hce1[36].append(BeautifulSoup('<div id="f_p1_jimok_actual" class="permit-cell-val" data-bind="jimok_actual" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt;" contenteditable="true"></div>', 'html.parser'))
    hce1[37].clear()
    hce1[37].append(BeautifulSoup('<div id="f_p1_land_ratio" class="permit-cell-val" data-bind="land_ratio_html" style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; line-height:3.6mm;" contenteditable="true"></div>', 'html.parser'))
    hce1[38].clear()
    hce1[38].append(BeautifulSoup('<div id="f_p1_yongdo" class="permit-cell-val" data-bind="yongdo_area" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:7.5pt; letter-spacing:-0.3px; padding:0 1mm;" contenteditable="true"></div>', 'html.parser'))
    hce1[39].clear()
    hce1[39].append(BeautifulSoup('<div id="f_p1_land_use" class="permit-cell-val" data-bind="land_use_status" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:7.5pt;" contenteditable="true"></div>', 'html.parser'))

    # Building & Rights
    hce1[50].clear()
    hce1[50].append(BeautifulSoup('<div id="f_p1_bld_type" class="permit-cell-val" data-bind="bld_type_short" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))
    hce1[51].clear()
    hce1[51].append(BeautifulSoup('<div id="f_p1_bld_unit" class="permit-cell-val" data-bind="bld_detail" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:7.5pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))
    hce1[52].clear()
    hce1[52].append(BeautifulSoup('<div id="f_p1_right_kind" class="permit-cell-val" data-bind="right_kind" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt;" contenteditable="true"></div>', 'html.parser'))
    hce1[53].clear()
    hce1[53].append(BeautifulSoup('<div id="f_p1_right_act" class="permit-cell-val" data-bind="right_action" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt;" contenteditable="true"></div>', 'html.parser'))

    # Circled numbers 21-30 replacements (clean Unicode ㉑~㉚, zero PUA tofu)
    hce1[58].clear()
    hce1[58].append(BeautifulSoup('<div class="hcD" style="left:1mm;top:1mm;"><div class="hcI" style="top:2.76mm;"><div class="hls ps25" style="line-height:2.79mm;white-space:nowrap;left:0mm;top:-0.18mm;height:3.53mm;width:26.25mm;"><span class="hrt cs14" style="font-family:\'Malgun Gothic\',\'Pretendard\',sans-serif;font-size:8.5pt;">㉓ 특기사항</span></div></div></div>', 'html.parser'))

    hce1[59].clear()
    hce1[59].append(BeautifulSoup('<div class="hcD" style="left:1mm;top:1mm;"><div class="hcI"><div class="hls ps25" style="line-height:2.79mm;white-space:nowrap;left:0mm;top:-0.18mm;height:3.53mm;width:34.30mm;"><span class="hrt cs14" style="font-family:\'Malgun Gothic\',\'Pretendard\',sans-serif;font-size:8.5pt;">㉑ 존속기간</span></div></div></div>', 'html.parser'))

    hce1[60].clear()
    hce1[60].append(BeautifulSoup('<div class="hcD" style="left:1mm;top:1mm;"><div class="hcI"><div class="hls ps25" style="line-height:2.79mm;white-space:nowrap;left:0mm;top:-0.18mm;height:3.53mm;width:32.58mm;"><span class="hrt cs14" style="font-family:\'Malgun Gothic\',\'Pretendard\',sans-serif;font-size:8.5pt;">㉒ 지대(연액)</span></div></div></div>', 'html.parser'))

    # Transfer type (in Cell 62 under Cell 56 "⑳소유권의 이전 또는 설정의 형태")
    hce1[62].clear()
    hce1[62].append(BeautifulSoup('<div id="f_p1_transfer_type" class="permit-cell-val" data-bind="transfer_type" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))

    hce1[71].clear()
    hce1[71].append(BeautifulSoup('<div class="hcD" style="left:1mm;top:1mm;"><div class="hcI" style="top:2.76mm;"><div class="hls ps25" style="line-height:2.79mm;white-space:nowrap;left:0mm;top:-0.18mm;height:3.53mm;width:26.25mm;"><span class="hrt cs14" style="font-family:\'Malgun Gothic\',\'Pretendard\',sans-serif;font-size:8.5pt;">㉚ 예정금액합계</span></div><div class="hls ps25" style="line-height:2.79mm;white-space:nowrap;left:0mm;top:3mm;height:3.53mm;width:26.25mm;"><span class="hrt cs14" style="font-family:\'Malgun Gothic\',\'Pretendard\',sans-serif;font-size:8pt;">(원)(㉗+㉙)</span></div></div></div>', 'html.parser'))

    hce1[72].clear()
    hce1[72].append(BeautifulSoup('<div class="hcD" style="left:1mm;top:1mm;"><div class="hcI"><div class="hls ps25" style="line-height:2.79mm;white-space:nowrap;left:0mm;top:-0.18mm;height:3.53mm;width:14.84mm;"><span class="hrt cs14" style="font-family:\'Malgun Gothic\',\'Pretendard\',sans-serif;font-size:8.5pt;">㉔ 지목</span></div><div class="hls ps25" style="line-height:2.79mm;white-space:nowrap;left:0mm;top:3mm;height:3.53mm;width:14.84mm;"><span class="hrt cs14" style="font-family:\'Malgun Gothic\',\'Pretendard\',sans-serif;font-size:8pt;">(현실)</span></div></div></div>', 'html.parser'))

    hce1[73].clear()
    hce1[73].append(BeautifulSoup('<div class="hcD" style="left:1mm;top:1mm;"><div class="hcI"><div class="hls ps25" style="line-height:2.79mm;white-space:nowrap;left:0mm;top:-0.18mm;height:3.53mm;width:15.61mm;"><span class="hrt cs14" style="font-family:\'Malgun Gothic\',\'Pretendard\',sans-serif;font-size:8.5pt;">㉕ 면적</span></div><div class="hls ps25" style="line-height:2.79mm;white-space:nowrap;left:0mm;top:3mm;height:3.53mm;width:15.61mm;"><span class="hrt cs14" style="font-family:\'Malgun Gothic\',\'Pretendard\',sans-serif;font-size:8pt;">(㎡)</span></div></div></div>', 'html.parser'))

    hce1[74].clear()
    hce1[74].append(BeautifulSoup('<div class="hcD" style="left:1mm;top:1mm;"><div class="hcI"><div class="hls ps25" style="line-height:2.79mm;white-space:nowrap;left:0mm;top:-0.18mm;height:3.53mm;width:17.46mm;"><span class="hrt cs14" style="font-family:\'Malgun Gothic\',\'Pretendard\',sans-serif;font-size:8.5pt;">㉖ 단가</span></div><div class="hls ps25" style="line-height:2.79mm;white-space:nowrap;left:0mm;top:3mm;height:3.53mm;width:17.46mm;"><span class="hrt cs14" style="font-family:\'Malgun Gothic\',\'Pretendard\',sans-serif;font-size:8pt;">(원/㎡)</span></div></div></div>', 'html.parser'))

    hce1[75].clear()
    hce1[75].append(BeautifulSoup('<div class="hcD" style="left:1mm;top:1mm;"><div class="hcI"><div class="hls ps25" style="line-height:2.79mm;white-space:nowrap;left:0mm;top:-0.18mm;height:3.53mm;width:22.80mm;"><span class="hrt cs14" style="font-family:\'Malgun Gothic\',\'Pretendard\',sans-serif;font-size:8.5pt;">㉗ 예정</span></div><div class="hls ps25" style="line-height:2.79mm;white-space:nowrap;left:0mm;top:3mm;height:3.53mm;width:22.80mm;"><span class="hrt cs14" style="font-family:\'Malgun Gothic\',\'Pretendard\',sans-serif;font-size:8pt;">금액(원)</span></div></div></div>', 'html.parser'))

    hce1[76].clear()
    hce1[76].append(BeautifulSoup('<div class="hcD" style="left:1mm;top:1mm;"><div class="hcI"><div class="hls ps25" style="line-height:2.79mm;white-space:nowrap;left:0mm;top:-0.18mm;height:3.53mm;width:11.46mm;"><span class="hrt cs14" style="font-family:\'Malgun Gothic\',\'Pretendard\',sans-serif;font-size:8.5pt;">㉘</span></div><div class="hls ps25" style="line-height:2.79mm;white-space:nowrap;left:0mm;top:3mm;height:3.53mm;width:11.46mm;"><span class="hrt cs14" style="font-family:\'Malgun Gothic\',\'Pretendard\',sans-serif;font-size:8pt;">종류</span></div></div></div>', 'html.parser'))

    hce1[77].clear()
    hce1[77].append(BeautifulSoup('<div class="hcD" style="left:1mm;top:1mm;"><div class="hcI"><div class="hls ps25" style="line-height:2.79mm;white-space:nowrap;left:0mm;top:-0.18mm;height:3.53mm;width:19.12mm;"><span class="hrt cs14" style="font-family:\'Malgun Gothic\',\'Pretendard\',sans-serif;font-size:8.5pt;">㉙ 예정</span></div><div class="hls ps25" style="line-height:2.79mm;white-space:nowrap;left:0mm;top:3mm;height:3.53mm;width:19.12mm;"><span class="hrt cs14" style="font-family:\'Malgun Gothic\',\'Pretendard\',sans-serif;font-size:8pt;">금액(원)</span></div></div></div>', 'html.parser'))

    # Prices
    hce1[79].clear()
    hce1[79].append(BeautifulSoup('<div class="permit-cell-val" data-bind="jimok_legal" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt;" contenteditable="true"></div>', 'html.parser'))
    hce1[80].clear()
    hce1[80].append(BeautifulSoup('<div class="permit-cell-val" data-bind="land_share_num" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))
    hce1[81].clear()
    hce1[81].append(BeautifulSoup('<div class="permit-cell-val" data-bind="land_unit_fmt" style="width:100%; height:100%; display:flex; align-items:center; justify-content:flex-end; padding-right:1mm; font-size:7.5pt;" contenteditable="true"></div>', 'html.parser'))
    hce1[82].clear()
    hce1[82].append(BeautifulSoup('<div class="permit-cell-val" data-bind="land_price_fmt" style="width:100%; height:100%; display:flex; align-items:center; justify-content:flex-end; padding-right:1mm; font-size:7.5pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))
    hce1[83].clear()
    hce1[83].append(BeautifulSoup('<div class="permit-cell-val" data-bind="bld_type_short" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:7.5pt;" contenteditable="true"></div>', 'html.parser'))
    hce1[84].clear()
    hce1[84].append(BeautifulSoup('<div class="permit-cell-val" data-bind="bld_price_fmt" style="width:100%; height:100%; display:flex; align-items:center; justify-content:flex-end; padding-right:1mm; font-size:7.5pt; letter-spacing:-0.4px; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))
    hce1[85].clear()
    hce1[85].append(BeautifulSoup('<div class="permit-cell-val" data-bind="total_price_fmt" style="width:100%; height:100%; display:flex; align-items:center; justify-content:flex-end; padding-right:1.5mm; font-size:7.8pt; letter-spacing:-0.3px; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))

    # P1 Date & Signatures
    hce1[95].clear()
    hce1[95].append(BeautifulSoup('<div class="permit-cell-val" id="f_p1_apply_date" data-bind="apply_date_fmt" style="width:100%; height:100%; display:flex; align-items:center; justify-content:flex-end; padding-right:15mm; font-size:10.5pt; font-family:\'맑은 고딕\',sans-serif; letter-spacing:1px; white-space:pre;" contenteditable="true"></div>', 'html.parser'))
    hce1[96].clear()
    hce1[96].append(BeautifulSoup('<div style="display:flex; justify-content:flex-end; align-items:center; width:100%; height:100%; padding-right:12mm; font-size:9pt;"><span style="margin-right:6mm;">매도인</span><span id="f_p1_seller_sign_names" style="font-weight:bold; min-width:60mm; white-space:nowrap; text-align:left;"></span><span style="color:#666; font-size:8.5pt; margin-left:3mm;">(서명 또는 인)</span></div>', 'html.parser'))
    hce1[97].clear()
    hce1[97].append(BeautifulSoup('<div style="display:flex; justify-content:flex-end; align-items:center; width:100%; height:100%; padding-right:12mm; font-size:9pt;"><span style="margin-right:6mm;">매수인</span><span id="f_p1_buyer_sign_names" style="font-weight:bold; min-width:60mm; white-space:nowrap; text-align:left;"></span><span style="color:#666; font-size:8.5pt; margin-left:3mm;">(서명 또는 인)</span></div>', 'html.parser'))

    # =========================================================================
    # 2. PAGE 2 (허가 신청서 - 별지목록)
    # =========================================================================
    p2 = pages[1]
    hce2 = p2.find_all('div', class_='hce')
    hce2[3].append(soup.new_tag('div', attrs={
        'id': 'f_p2_seller2_name', 'class': 'permit-cell-val', 'data-bind': 'seller2_name',
        'style': 'position:absolute; left:25mm; top:0; width:calc(100% - 26mm); height:100%; display:flex; align-items:center; font-size:8.5pt; font-weight:bold;',
        'contenteditable': 'true'
    }))
    hce2[4].append(soup.new_tag('div', attrs={
        'id': 'f_p2_seller2_rrn', 'class': 'permit-cell-val', 'data-bind': 'seller2_rrn',
        'style': 'position:absolute; left:0; bottom:1.5mm; width:100%; height:5mm; display:flex; align-items:center; justify-content:center; font-size:8.5pt;',
        'contenteditable': 'true'
    }))
    hce2[5].append(soup.new_tag('div', attrs={
        'id': 'f_p2_seller2_addr', 'class': 'permit-cell-val', 'data-bind': 'seller2_addr',
        'style': 'position:absolute; left:1mm; bottom:1.5mm; width:calc(100% - 2mm); height:6mm; display:flex; align-items:center; font-size:7.5pt; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;',
        'contenteditable': 'true'
    }))
    hce2[6].append(soup.new_tag('div', attrs={
        'id': 'f_p2_seller2_tel', 'class': 'permit-cell-val', 'data-bind': 'seller2_tel',
        'style': 'position:absolute; left:0; bottom:1.5mm; width:100%; height:5mm; display:flex; align-items:center; justify-content:center; font-size:8.5pt;',
        'contenteditable': 'true'
    }))

    hce2[24].append(soup.new_tag('div', attrs={
        'id': 'f_p2_buyer2_name', 'class': 'permit-cell-val', 'data-bind': 'buyer2_name',
        'style': 'position:absolute; left:25mm; top:0; width:calc(100% - 26mm); height:100%; display:flex; align-items:center; font-size:8.5pt; font-weight:bold;',
        'contenteditable': 'true'
    }))
    hce2[25].append(soup.new_tag('div', attrs={
        'id': 'f_p2_buyer2_rrn', 'class': 'permit-cell-val', 'data-bind': 'buyer2_rrn',
        'style': 'position:absolute; left:0; bottom:1.5mm; width:100%; height:5mm; display:flex; align-items:center; justify-content:center; font-size:8.5pt;',
        'contenteditable': 'true'
    }))
    hce2[26].append(soup.new_tag('div', attrs={
        'id': 'f_p2_buyer2_addr', 'class': 'permit-cell-val', 'data-bind': 'buyer2_addr',
        'style': 'position:absolute; left:1mm; bottom:1.5mm; width:calc(100% - 2mm); height:6mm; display:flex; align-items:center; font-size:7.5pt; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;',
        'contenteditable': 'true'
    }))
    hce2[27].append(soup.new_tag('div', attrs={
        'id': 'f_p2_buyer2_tel', 'class': 'permit-cell-val', 'data-bind': 'buyer2_tel',
        'style': 'position:absolute; left:0; bottom:1.5mm; width:100%; height:5mm; display:flex; align-items:center; justify-content:center; font-size:8.5pt;',
        'contenteditable': 'true'
    }))

    # =========================================================================
    # 3. PAGE 3 (토지취득자금 조달계획서 - 매수인 1)
    # =========================================================================
    p3 = pages[2]
    hce3 = p3.find_all('div', class_='hce')
    hce3[3].append(soup.new_tag('div', attrs={
        'id': 'f_p3_buyer_name', 'class': 'permit-cell-val', 'data-bind': 'p3_submitter_name',
        'style': 'position:absolute; left:25mm; top:0; width:calc(100% - 26mm); height:100%; display:flex; align-items:center; font-size:8.5pt; font-weight:bold;',
        'contenteditable': 'true'
    }))
    hce3[4].append(soup.new_tag('div', attrs={
        'id': 'f_p3_buyer_rrn', 'class': 'permit-cell-val', 'data-bind': 'p3_submitter_rrn',
        'style': 'position:absolute; left:0; bottom:1mm; width:100%; height:4.5mm; display:flex; align-items:center; justify-content:center; font-size:8.5pt;',
        'contenteditable': 'true'
    }))
    hce3[5].append(soup.new_tag('div', attrs={
        'id': 'f_p3_buyer_addr', 'class': 'permit-cell-val', 'data-bind': 'p3_submitter_addr',
        'style': 'position:absolute; left:1mm; bottom:1mm; width:calc(100% - 2mm); height:4.5mm; display:flex; align-items:center; font-size:7.5pt; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;',
        'contenteditable': 'true'
    }))
    hce3[6].append(soup.new_tag('div', attrs={
        'id': 'f_p3_buyer_tel', 'class': 'permit-cell-val', 'data-bind': 'p3_submitter_tel',
        'style': 'position:absolute; left:0; bottom:1mm; width:100%; height:4.5mm; display:flex; align-items:center; justify-content:center; font-size:8.5pt;',
        'contenteditable': 'true'
    }))

    # Funding values inside cells (slightly lowered with top:1.5mm)
    hce3[9].append(soup.new_tag('div', attrs={
        'class': 'permit-cell-val', 'data-bind': 'fund_deposit_fmt',
        'style': 'position:absolute; right:7mm; top:1.5mm; height:calc(100% - 1.5mm); display:flex; align-items:center; font-size:8pt; font-weight:bold;'
    }))
    hce3[10].append(soup.new_tag('div', attrs={
        'class': 'permit-cell-val', 'data-bind': 'fund_stocks_fmt',
        'style': 'position:absolute; right:7mm; top:1.5mm; height:calc(100% - 1.5mm); display:flex; align-items:center; font-size:8pt; font-weight:bold;'
    }))
    hce3[13].append(soup.new_tag('div', attrs={
        'class': 'permit-cell-val', 'data-bind': 'fund_gift_fmt',
        'style': 'position:absolute; right:7mm; top:1.5mm; height:calc(100% - 1.5mm); display:flex; align-items:center; font-size:8pt; font-weight:bold;'
    }))
    hce3[17].append(soup.new_tag('div', attrs={
        'class': 'permit-cell-val', 'data-bind': 'fund_realestate_fmt',
        'style': 'position:absolute; right:7mm; top:1.5mm; height:calc(100% - 1.5mm); display:flex; align-items:center; font-size:8pt; font-weight:bold;'
    }))
    hce3[23].append(soup.new_tag('div', attrs={
        'class': 'permit-cell-val', 'data-bind': 'fund_loan_fmt',
        'style': 'position:absolute; right:7mm; top:1.5mm; height:calc(100% - 1.5mm); display:flex; align-items:center; font-size:8pt; font-weight:bold;'
    }))
    hce3[32].append(soup.new_tag('div', attrs={
        'class': 'permit-cell-val', 'data-bind': 'fund_borrow_fmt',
        'style': 'position:absolute; right:7mm; top:1.5mm; height:calc(100% - 1.5mm); display:flex; align-items:center; font-size:8pt; font-weight:bold;'
    }))
    hce3[37].append(soup.new_tag('div', attrs={
        'class': 'permit-cell-val', 'data-bind': 'fund_total_fmt',
        'style': 'position:absolute; right:7mm; top:1.5mm; height:calc(100% - 1.5mm); display:flex; align-items:center; font-size:8.5pt; font-weight:bold;'
    }))

    # Date and signature
    hce3[39].clear()
    hce3[39].append(BeautifulSoup('<div class="permit-cell-val" id="f_p3_submit_date" data-bind="apply_date_fmt" style="width:100%; height:100%; display:flex; align-items:center; justify-content:flex-end; padding-right:15mm; font-size:9.5pt; font-family:\'맑은 고딕\',sans-serif; white-space:pre;" contenteditable="true"></div>', 'html.parser'))
    hce3[41].clear()
    hce3[41].append(BeautifulSoup('<div style="display:flex; justify-content:flex-end; align-items:center; width:100%; height:100%; padding-right:15mm; font-size:9pt;"><span id="f_p3_sign_name" data-bind="p3_submitter_name" style="font-weight:bold; margin-right:8mm;"></span><span style="color:#666; font-size:8.5pt;">(서명 또는 인)</span></div>', 'html.parser'))

    # Clone Page 3 for Buyer 2 (Page 3-2)
    p3_2 = copy.deepcopy(p3)
    p3_2['id'] = 'page_3_2'
    p3_2['data-page'] = '3-2'
    cls_list = p3_2.get('class', [])
    if isinstance(cls_list, str):
        cls_list = cls_list.split()
    p3_2['class'] = cls_list + ['p3-buyer2-page']
    p3_2['style'] = (p3_2.get('style', '') + '; display:none;').strip(';')
    
    # Update data-binds in p3_2
    for el in p3_2.find_all(attrs={'data-bind': True}):
        b = el['data-bind']
        if b == 'p3_submitter_name':
            el['data-bind'] = 'p3_2_submitter_name'
        elif b == 'p3_submitter_rrn':
            el['data-bind'] = 'p3_2_submitter_rrn'
        elif b == 'p3_submitter_addr':
            el['data-bind'] = 'p3_2_submitter_addr'
        elif b == 'p3_submitter_tel':
            el['data-bind'] = 'p3_2_submitter_tel'
        elif b == 'fund_deposit_fmt':
            el['data-bind'] = 'fund2_deposit_fmt'
        elif b == 'fund_stocks_fmt':
            el['data-bind'] = 'fund2_stocks_fmt'
        elif b == 'fund_gift_fmt':
            el['data-bind'] = 'fund2_gift_fmt'
        elif b == 'fund_realestate_fmt':
            el['data-bind'] = 'fund2_realestate_fmt'
        elif b == 'fund_loan_fmt':
            el['data-bind'] = 'fund2_loan_fmt'
        elif b == 'fund_borrow_fmt':
            el['data-bind'] = 'fund2_borrow_fmt'
        elif b == 'fund_total_fmt' or b == 'total_price_fmt':
            el['data-bind'] = 'fund2_total_fmt'

    sign2 = p3_2.find(id='f_p3_sign_name')
    if sign2:
        sign2['id'] = 'f_p3_2_sign_name'
        sign2['data-bind'] = 'p3_2_submitter_name'
    sub_date2 = p3_2.find(id='f_p3_submit_date')
    if sub_date2:
        sub_date2['id'] = 'f_p3_2_submit_date'

    # =========================================================================
    # 4. PAGE 4 (토지이용계획서 A)
    # =========================================================================
    p4 = pages[3]
    hce4 = p4.find_all('div', class_='hce')
    hce4[2].clear()
    hce4[2].append(BeautifulSoup('<div id="f_p4_buyer_name" class="permit-cell-val" data-bind="p4_buyer_names_fmt" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8.5pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))
    hce4[4].clear()
    hce4[4].append(BeautifulSoup('<div id="f_p4_buyer_rrn" class="permit-cell-val" data-bind="p4_buyer_rrns_html" style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; font-size:7pt; line-height:3.5mm;" contenteditable="true"></div>', 'html.parser'))
    hce4[6].clear()
    hce4[6].append(BeautifulSoup('<div id="f_p4_buyer_tel" class="permit-cell-val" data-bind="p4_buyer_tels_html" style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; font-size:7pt; line-height:3.5mm;" contenteditable="true"></div>', 'html.parser'))
    hce4[8].clear()
    hce4[8].append(BeautifulSoup('<div id="f_p4_buyer_addr" class="permit-cell-val" data-bind="buyer_addr" style="width:100%; height:100%; display:flex; align-items:center; padding-left:2mm; font-size:8pt;" contenteditable="true"></div>', 'html.parser'))

    hce4[17].clear()
    hce4[17].append(BeautifulSoup('<div id="f_p4_dong_jibun" class="permit-cell-val" data-bind="dong_jibun" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))
    hce4[18].clear()
    hce4[18].append(BeautifulSoup('<div class="permit-cell-val" data-bind="jimok_legal" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt;" contenteditable="true"></div>', 'html.parser'))
    hce4[19].clear()
    hce4[19].append(BeautifulSoup('<div class="permit-cell-val" data-bind="jimok_actual" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt;" contenteditable="true"></div>', 'html.parser'))
    hce4[20].clear()
    hce4[20].append(BeautifulSoup('<div class="permit-cell-val" data-bind="land_share_display" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))
    hce4[21].clear()
    hce4[21].append(BeautifulSoup('<div class="permit-cell-val" data-bind="yongdo_area" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:7.5pt;" contenteditable="true"></div>', 'html.parser'))
    hce4[22].clear()
    hce4[22].append(BeautifulSoup('<div class="permit-cell-val" data-bind="bld_desc" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:7.5pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))

    # Purpose, Dates
    hce4[27].clear()
    hce4[27].append(BeautifulSoup('<div class="permit-cell-val" data-bind="purpose" style="width:100%; height:100%; display:flex; align-items:center; padding-left:2mm; font-size:8pt;" contenteditable="true"></div>', 'html.parser'))
    hce4[40].clear()
    hce4[40].append(BeautifulSoup('<div class="permit-cell-val" data-bind="balance_date" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt;" contenteditable="true"></div>', 'html.parser'))
    hce4[44].clear()
    hce4[44].append(BeautifulSoup('<div class="permit-cell-val" data-bind="move_in_date" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt;" contenteditable="true"></div>', 'html.parser'))
    hce4[55].clear()
    hce4[55].append(BeautifulSoup('<div class="permit-cell-val" data-bind="tenant_vacate" style="width:100%; height:100%; display:flex; align-items:center; padding-left:2mm; font-size:8pt;" contenteditable="true"></div>', 'html.parser'))

    # Bottom date and signature on Page 4
    for d in p4.find_all('div', class_='ps109'):
        d.clear()
        d.append(BeautifulSoup('<div style="width:100%; display:flex; justify-content:flex-end; padding-right:15mm; font-size:10pt; font-family:\'맑은 고딕\',sans-serif; white-space:pre;"><span data-bind="apply_date_fmt"></span></div>', 'html.parser'))

    for span in p4.find_all('span', class_='hrt'):
        if '(서명 또는 인)' in span.get_text():
            p_elem = span.find_parent('div', class_='hls')
            if p_elem:
                p_elem.clear()
                p_elem.append(BeautifulSoup('<div id="f_p4_sign_container" style="display:flex; justify-content:flex-end; align-items:flex-start; width:100%; padding-right:15mm; font-size:9pt;"></div>', 'html.parser'))

    # =========================================================================
    # 5. PAGE 5 (토지이용계획서 B)
    # =========================================================================
    p5 = pages[4]
    hce5 = p5.find_all('div', class_='hce')
    hce5[2].clear()
    hce5[2].append(BeautifulSoup('<div id="f_p5_seller_name" class="permit-cell-val" data-bind="p5_seller_names_html" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8.5pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))
    hce5[4].clear()
    hce5[4].append(BeautifulSoup('<div id="f_p5_seller_rrn" class="permit-cell-val" data-bind="p5_seller_rrns_html" style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; font-size:7.5pt; line-height:3.5mm;" contenteditable="true"></div>', 'html.parser'))
    hce5[6].clear()
    hce5[6].append(BeautifulSoup('<div id="f_p5_seller_tel" class="permit-cell-val" data-bind="p5_seller_tels_html" style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; font-size:7.5pt; line-height:3.5mm;" contenteditable="true"></div>', 'html.parser'))
    hce5[8].clear()
    hce5[8].append(BeautifulSoup('<div id="f_p5_seller_addr" class="permit-cell-val" data-bind="seller_addr" style="width:100%; height:100%; display:flex; align-items:center; padding-left:2mm; font-size:8pt;" contenteditable="true"></div>', 'html.parser'))

    # Bottom signatures on Page 5
    for span in p5.find_all('span', class_='hrt'):
        txt = span.get_text()
        if '매도인 :' in txt:
            p_elem = span.find_parent('div', class_='hls')
            if p_elem:
                p_elem.clear()
                p_elem.append(BeautifulSoup('<div style="display:flex; justify-content:flex-end; align-items:center; width:100%; padding-right:15mm; font-size:9pt;"><span style="margin-right:8mm;">매도인 :</span><span id="f_p5_sign_seller_names" style="font-weight:bold; min-width:60mm; white-space:nowrap; text-align:left;"></span><span style="color:#666; font-size:8.5pt; margin-left:3mm;">(인)</span></div>', 'html.parser'))
        elif '매수인 :' in txt:
            p_elem = span.find_parent('div', class_='hls')
            if p_elem:
                p_elem.clear()
                p_elem.append(BeautifulSoup('<div style="display:flex; justify-content:flex-end; align-items:center; width:100%; padding-right:15mm; font-size:9pt;"><span style="margin-right:8mm;">매수인 :</span><span id="f_p5_sign_buyer_names" style="font-weight:bold; min-width:60mm; white-space:nowrap; text-align:left;"></span><span style="color:#666; font-size:8.5pt; margin-left:3mm;">(인)</span></div>', 'html.parser'))
    # Clean table dates on Page 5 (수기 작성용 공백 '      년      월      일')
    for c in p5.find_all('div', class_='hce'):
        for sp in c.find_all('span', class_='hrt'):
            if '202' in sp.get_text() and '년' in sp.get_text():
                sp.string = '      년      월      일'

    # Date on Page 5 (우측 정렬)
    for d in p5.find_all('div', class_='ps66'):
        d.clear()
        d.append(BeautifulSoup('<div style="width:100%; display:flex; justify-content:flex-end; padding-right:15mm; font-size:10pt; font-family:\'맑은 고딕\',sans-serif; white-space:pre;"><span data-bind="apply_date_fmt"></span></div>', 'html.parser'))

    # =========================================================================
    # 6. PAGE 6 (주택 임대차 계약 확인서)
    # =========================================================================
    p6 = pages[5]
    hce6 = p6.find_all('div', class_='hce')
    hce6[2].clear()
    hce6[2].append(BeautifulSoup('<div id="f_p6_addr" class="permit-cell-val" data-bind="addr_full" style="width:100%; height:100%; display:flex; align-items:center; padding-left:2mm; font-size:8pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))
    hce6[4].clear()
    hce6[4].append(BeautifulSoup('<div id="f_p6_land_area" class="permit-cell-val" data-bind="land_share_num" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))
    hce6[6].clear()
    hce6[6].append(BeautifulSoup('<div id="f_p6_bld_area" class="permit-cell-val" data-bind="exclusive_area" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))

    hce6[14].clear()
    hce6[14].append(BeautifulSoup('<div id="f_p6_landlord_name" class="permit-cell-val" data-bind="p6_landlord_name_html" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8.5pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))
    hce6[16].clear()
    hce6[16].append(BeautifulSoup('<div id="f_p6_landlord_birth" class="permit-cell-val" data-bind="p6_landlord_birth_html" style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; font-size:7.5pt; line-height:3.5mm;" contenteditable="true"></div>', 'html.parser'))
    hce6[18].clear()
    hce6[18].append(BeautifulSoup('<div id="f_p6_landlord_addr" class="permit-cell-val" data-bind="p6_landlord_addr_html" style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; padding-left:2mm; font-size:7.5pt;" contenteditable="true"></div>', 'html.parser'))
    hce6[20].clear()
    hce6[20].append(BeautifulSoup('<div id="f_p6_landlord_tel" class="permit-cell-val" data-bind="p6_landlord_tel_html" style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; padding-left:2mm; font-size:7.5pt; line-height:3.5mm;" contenteditable="true"></div>', 'html.parser'))

    # Bottom signatures on Page 6
    for span in p6.find_all('span', class_='hrt'):
        txt = span.get_text()
        if '임대인 :' in txt:
            p_elem = span.find_parent('div', class_='hls')
            if p_elem:
                p_elem['id'] = 'f_p6_sign_wrapper'
                p_elem['style'] = 'line-height:3.76mm;white-space:nowrap;left:0mm;top:215mm;width:180mm;'
                p_elem.clear()
                p_elem.append(BeautifulSoup('<div id="f_p6_sign_container" style="width:100%;"></div>', 'html.parser'))
        elif '임차인 :' in txt:
            p_elem = span.find_parent('div', class_='hls')
            if p_elem:
                p_elem.decompose()
        elif '동안구청장' in txt:
            p_elem = span.find_parent('div', class_='hls')
            if p_elem:
                p_elem['id'] = 'f_p6_recipient'
                p_elem['style'] = 'line-height:5.52mm;white-space:nowrap;left:0mm;top:235mm;height:6.35mm;width:180mm;'

    # Date on Page 6 (우측 정렬)
    for d in p6.find_all('div', class_='ps90'):
        if '년' in d.get_text() and '월' in d.get_text() and '임대' not in d.get_text() and '임차' not in d.get_text():
            d.clear()
            d.append(BeautifulSoup('<div style="width:100%; display:flex; justify-content:flex-end; padding-right:15mm; font-size:10pt; font-family:\'맑은 고딕\',sans-serif; white-space:pre;"><span data-bind="apply_date_fmt"></span></div>', 'html.parser'))

    # =========================================================================
    # 7. PAGE 7 (개인정보동의서)
    # =========================================================================
    p7 = pages[6]
    hce7 = p7.find_all('div', class_='hce')
    
    # 신청인 좌측 셀 폰트/굵기 보장 (15pt bold 맑은 고딕)
    span_applicant = hce7[24].find('span', class_='hrt')
    if span_applicant:
        span_applicant['style'] = "font-size:15pt; font-family:'맑은 고딕','Malgun Gothic',sans-serif; font-weight:bold;"

    # 신청인 우측 성명/주민번호/연락처 셀 원본 서식 완벽 복원 (13pt bold, (서명 또는 인) 13pt normal 우측 정렬)
    hce7[25].clear()
    hce7[25].append(BeautifulSoup('''<div class="hcD" style="left:1.80mm;top:0.50mm;">
      <div class="hcI" style="top:2.99mm;">
        <div class="hls ps1" style="line-height:3.76mm;white-space:nowrap;left:0mm;top:-0.23mm;height:4.59mm;width:151.44mm;display:flex;align-items:center;">
          <span class="hrt cs153" style="font-size:13pt;font-family:'맑은 고딕','Malgun Gothic',sans-serif;font-weight:bold;white-space:pre;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;성 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;명 : </span>
          <span data-bind="p7_buyer_name" class="hrt cs153" style="font-size:13pt;font-family:'맑은 고딕','Malgun Gothic',sans-serif;font-weight:bold;min-width:32mm;display:inline-block;"></span>
          <span class="hrt cs63" style="font-size:13pt;font-family:'맑은 고딕','Malgun Gothic',sans-serif;font-weight:normal;margin-left:auto;margin-right:12mm;">(서명 또는 인)</span>
        </div>
        <div class="hls ps1" style="line-height:3.76mm;white-space:nowrap;left:0mm;top:7.11mm;height:4.59mm;width:151.44mm;display:flex;align-items:center;">
          <span class="hrt cs153" style="font-size:13pt;font-family:'맑은 고딕','Malgun Gothic',sans-serif;font-weight:bold;white-space:pre;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;주민등록번호 : </span>
          <span data-bind="p7_buyer_rrn" class="hrt cs153" style="font-size:13pt;font-family:'맑은 고딕','Malgun Gothic',sans-serif;font-weight:bold;"></span>
        </div>
        <div class="hls ps1" style="line-height:3.76mm;white-space:nowrap;left:0mm;top:14.45mm;height:4.59mm;width:151.44mm;display:flex;align-items:center;">
          <span class="hrt cs153" style="font-size:13pt;font-family:'맑은 고딕','Malgun Gothic',sans-serif;font-weight:bold;white-space:pre;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;전 화 번 호 &nbsp;: </span>
          <span data-bind="p7_buyer_tel" class="hrt cs153" style="font-size:13pt;font-family:'맑은 고딕','Malgun Gothic',sans-serif;font-weight:bold;"></span>
        </div>
      </div>
    </div>''', 'html.parser'))

    # Date on Page 7 (우측 정렬)
    for div in p7.find_all('div', class_='ps49'):
        if not div.find_parent('div', class_='hce') and ('202' in div.get_text() or '년' in div.get_text()):
            div.clear()
            div.append(BeautifulSoup('<div style="width:100%; display:flex; justify-content:flex-end; padding-right:15mm; font-size:12pt; font-family:\'맑은 고딕\',sans-serif; white-space:pre;"><span data-bind="apply_date_fmt"></span></div>', 'html.parser'))

    # Clone Page 7 for Buyer 2 (Page 7-2)
    p7_2 = copy.deepcopy(p7)
    p7_2['id'] = 'page_7_2'
    p7_2['data-page'] = '7-2'
    cls_list7 = p7_2.get('class', [])
    if isinstance(cls_list7, str):
        cls_list7 = cls_list7.split()
    p7_2['class'] = cls_list7 + ['p7-buyer2-page']
    p7_2['style'] = (p7_2.get('style', '') + '; display:none;').strip(';')

    # Update data-binds in p7_2
    for el in p7_2.find_all(attrs={'data-bind': True}):
        b = el['data-bind']
        if b == 'p7_buyer_name':
            el['data-bind'] = 'p7_2_buyer_name'
        elif b == 'p7_buyer_rrn':
            el['data-bind'] = 'p7_2_buyer_rrn'
        elif b == 'p7_buyer_tel':
            el['data-bind'] = 'p7_2_buyer_tel'

    # =========================================================================
    # 8. PAGE 8 (위임장)
    # =========================================================================
    p8 = pages[7]
    hce8 = p8.find_all('div', class_='hce')
    # Seller
    hce8[1].clear()
    hce8[1].append(BeautifulSoup('<div id="f_p8_seller_name" class="permit-cell-val" data-bind="p8_seller_names_fmt" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))
    hce8[3].clear()
    hce8[3].append(BeautifulSoup('<div id="f_p8_seller_rrn" class="permit-cell-val" data-bind="p8_seller_rrns_fmt" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:7.5pt;" contenteditable="true"></div>', 'html.parser'))
    hce8[5].clear()
    hce8[5].append(BeautifulSoup('<div id="f_p8_seller_addr" class="permit-cell-val" data-bind="seller_addr" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:7.5pt; padding:0 1mm;" contenteditable="true"></div>', 'html.parser'))
    hce8[7].clear()
    hce8[7].append(BeautifulSoup('<div id="f_p8_seller_tel" class="permit-cell-val" data-bind="p8_seller_tels_fmt" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:7pt; letter-spacing:-0.2px;" contenteditable="true"></div>', 'html.parser'))

    # Buyer
    hce8[9].clear()
    hce8[9].append(BeautifulSoup('<div id="f_p8_buyer_name" class="permit-cell-val" data-bind="p8_buyer_names_fmt" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))
    hce8[11].clear()
    hce8[11].append(BeautifulSoup('<div id="f_p8_buyer_rrn" class="permit-cell-val" data-bind="p8_buyer_rrns_fmt" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:7.5pt;" contenteditable="true"></div>', 'html.parser'))
    hce8[13].clear()
    hce8[13].append(BeautifulSoup('<div id="f_p8_buyer_addr" class="permit-cell-val" data-bind="buyer_addr" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:7.5pt; padding:0 1mm;" contenteditable="true"></div>', 'html.parser'))
    hce8[15].clear()
    hce8[15].append(BeautifulSoup('<div id="f_p8_buyer_tel" class="permit-cell-val" data-bind="p8_buyer_tels_fmt" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:7pt; letter-spacing:-0.2px;" contenteditable="true"></div>', 'html.parser'))

    # Agent (수임인 인적사항: 주민등록번호는 agent_rrn!)
    hce8[17].clear()
    hce8[17].append(BeautifulSoup('<div class="permit-cell-val" data-bind="agent_name" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8.5pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))
    hce8[19].clear()
    hce8[19].append(BeautifulSoup('<div class="permit-cell-val" data-bind="agent_rrn" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:8pt;" contenteditable="true"></div>', 'html.parser'))
    hce8[21].clear()
    hce8[21].append(BeautifulSoup('<div class="permit-cell-val" data-bind="agent_addr" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:7.5pt; padding:0 1mm; text-align:center;" contenteditable="true"></div>', 'html.parser'))
    hce8[23].clear()
    hce8[23].append(BeautifulSoup('<div class="permit-cell-val" data-bind="agent_tel" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:7.5pt;" contenteditable="true"></div>', 'html.parser'))

    # Property
    hce8[25].clear()
    hce8[25].append(BeautifulSoup('<div class="permit-cell-val" data-bind="addr_full" style="width:100%; height:100%; display:flex; align-items:center; padding-left:2mm; font-size:8pt; font-weight:bold;" contenteditable="true"></div>', 'html.parser'))

    # Bottom signatures on Page 8 (위임인/수임인 위치, 12pt 글씨크기, 굵기 및 정렬 완벽 복원)
    for span in p8.find_all('span', class_='hrt'):
        txt = span.get_text()
        if '위임인 - 매도인' in txt:
            p_elem = span.find_parent('div', class_='hls')
            if p_elem:
                p_elem.clear()
                p_elem.append(BeautifulSoup('''<div style="display:flex; align-items:center; width:100%; padding-left:18mm; padding-right:14mm; font-size:12pt; font-family:'맑은 고딕','Malgun Gothic',sans-serif; line-height:1;">
                  <span style="display:inline-block; width:18mm; font-weight:bold; white-space:nowrap;">위임인</span>
                  <span style="display:inline-block; width:22mm; font-weight:bold; white-space:nowrap;">- 매도인</span>
                  <span style="display:inline-block; width:18mm; font-weight:bold; white-space:nowrap;">성명:</span>
                  <span id="f_p8_sign_seller_names" style="font-weight:bold; min-width:50mm; text-align:left; white-space:nowrap;"></span>
                  <span style="font-weight:normal; margin-left:auto; white-space:nowrap;">(서명 또는 인)</span>
                </div>''', 'html.parser'))
        elif '- 매수인' in txt:
            p_elem = span.find_parent('div', class_='hls')
            if p_elem:
                p_elem.clear()
                p_elem.append(BeautifulSoup('''<div style="display:flex; align-items:center; width:100%; padding-left:18mm; padding-right:14mm; font-size:12pt; font-family:'맑은 고딕','Malgun Gothic',sans-serif; line-height:1;">
                  <span style="display:inline-block; width:18mm; font-weight:bold; white-space:nowrap; visibility:hidden;">위임인</span>
                  <span style="display:inline-block; width:22mm; font-weight:bold; white-space:nowrap;">- 매수인</span>
                  <span style="display:inline-block; width:18mm; font-weight:bold; white-space:nowrap;">성명:</span>
                  <span id="f_p8_sign_buyer_names" style="font-weight:bold; min-width:50mm; text-align:left; white-space:nowrap;"></span>
                  <span style="font-weight:normal; margin-left:auto; white-space:nowrap;">(서명 또는 인)</span>
                </div>''', 'html.parser'))
        elif '수임인' in txt and '성명:' in txt:
            p_elem = span.find_parent('div', class_='hls')
            if p_elem:
                p_elem.clear()
                p_elem.append(BeautifulSoup('''<div style="display:flex; align-items:center; width:100%; padding-left:18mm; padding-right:14mm; font-size:12pt; font-family:'맑은 고딕','Malgun Gothic',sans-serif; line-height:1;">
                  <span style="display:inline-block; width:18mm; font-weight:bold; white-space:nowrap;">수임인</span>
                  <span style="display:inline-block; width:22mm; font-weight:bold; white-space:nowrap; visibility:hidden;">- 매도인</span>
                  <span style="display:inline-block; width:18mm; font-weight:bold; white-space:nowrap;">성명:</span>
                  <span id="f_p8_sign_agent_name" data-bind="agent_name" style="font-weight:bold; min-width:50mm; text-align:left; white-space:nowrap;"></span>
                  <span style="font-weight:normal; margin-left:auto; white-space:nowrap;">(서명 또는 인)</span>
                </div>''', 'html.parser'))

    # Date on Page 8 (우측 정렬)
    for div in p8.find_all('div', class_='ps49'):
        if not div.find_parent('div', class_='hce') and ('202' in div.get_text() or '년' in div.get_text()):
            div.clear()
            div.append(BeautifulSoup('<div style="width:100%; display:flex; justify-content:flex-end; padding-right:15mm; font-size:11pt; font-family:\'맑은 고딕\',sans-serif; white-space:pre;"><span data-bind="apply_date_fmt"></span></div>', 'html.parser'))

    # Insert cloned Page 3-2 after Page 3 (index 3)
    pages.insert(3, p3_2)
    # Insert cloned Page 7-2 after Page 7 (index 8)
    pages.insert(8, p7_2)

    # Mark pages with IDs and data-page
    page_id_map = ['page_1', 'page_2', 'page_3', 'page_3_2', 'page_4', 'page_5', 'page_6', 'page_7', 'page_7_2', 'page_8']
    data_page_map = ['1', '2', '3', '3-2', '4', '5', '6', '7', '7-2', '8']
    for p, pid, dpage in zip(pages, page_id_map, data_page_map):
        p['id'] = pid
        p['data-page'] = dpage

    pages_html = "\n".join(str(p) for p in pages)
    with open('toji-permit/build_scripts/pages_built.html', 'w', encoding='utf-8') as f:
        f.write(pages_html)
    print("toji-permit/build_scripts/pages_built.html created with 100% cell-injected layout!")

if __name__ == '__main__':
    build_permit()
