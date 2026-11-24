import os
import sys
import glob
import fitz  # PyMuPDF

def convert_pdf_to_images(pdf_path=None, output_dir="bg", dpi=300):
    os.makedirs(output_dir, exist_ok=True)
    
    # PDF 경로 미지정 시 루트 및 상위 디렉터리에서 자동 탐색
    if not pdf_path:
        candidates = glob.glob("*토지거래허가신청서*.pdf") + glob.glob("../*토지거래허가신청서*.pdf") + glob.glob("*.pdf")
        if candidates:
            pdf_path = candidates[0]
            print(f"[*] PDF 파일을 자동으로 감지했습니다: {pdf_path}")
        else:
            print("[!] 변환할 PDF 파일을 찾지 못했습니다.")
            print("    사용법: python convert_pdf_to_bg.py <PDF_파일경로>")
            return False

    if not os.path.exists(pdf_path):
        print(f"[!] 파일을 찾을 수 없습니다: {pdf_path}")
        return False

    print(f"[*] PDF 변환 시작: {pdf_path} (DPI: {dpi})")
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    print(f"[*] 총 {total_pages} 페이지 감지됨.")

    # 72 DPI 기준 zoom 계수 계산
    zoom = dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)

    for i, page in enumerate(doc):
        page_num = i + 1
        pix = page.get_pixmap(matrix=mat, alpha=False)
        out_path = os.path.join(output_dir, f"page_{page_num}.png")
        pix.save(out_path)
        print(f"    [P.{page_num}/{total_pages}] 저장 완료 -> {out_path} ({pix.width}x{pix.height})")

    print(f"[+] 변환 완료! 총 {total_pages}개 파일이 '{output_dir}' 폴더에 저장되었습니다.")
    return True

if __name__ == "__main__":
    target_pdf = sys.argv[1] if len(sys.argv) > 1 else None
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)
    convert_pdf_to_images(target_pdf, output_dir="bg", dpi=300)
