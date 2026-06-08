import os

def extract_png_from_z9s(file_path, output_dir):
    with open(file_path, 'rb') as f:
        data = f.read()
    
    # PNG 파일의 시작(Header)과 끝(Trailer) 바이너리 시그니처
    png_header = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
    png_trailer = b'\x49\x45\x4E\x44\xAE\x42\x60\x82'
    
    start_idx = 0
    file_count = 0
    
    # 입력 파일명 추출 (예: B_Shoe005.Z9S -> B_Shoe005)
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    
    while True:
        # 데이터 내에서 PNG 시작 지점 검색
        start_idx = data.find(png_header, start_idx)
        if start_idx == -1:
            break
            
        # 데이터 내에서 PNG 끝 지점 검색
        end_idx = data.find(png_trailer, start_idx)
        if end_idx == -1:
            break
            
        # Trailer의 길이(8바이트)만큼 더해줌
        end_idx += len(png_trailer)
        
        # PNG 데이터 추출
        png_data = data[start_idx:end_idx]
        
        # 출력 파일명 및 전체 경로 설정 (MyPytheonExtractDocument 폴더 바로 아래 저장)
        output_filename = f"{base_name}_extracted_{file_count}.png"
        output_path = os.path.join(output_dir, output_filename)
        
        # 파일 저장
        with open(output_path, 'wb') as out_f:
            out_f.write(png_data)
            
        print(f"추출 완료: {output_path}")
        file_count += 1
        start_idx = end_idx  # 다음 파일 검색을 위해 인덱스 이동

if __name__ == "__main__":
    # 요구하신 폴더 경로 설정
    source_dir = r"D:\제1작업실\LT．／LCDR．Hinamori Amu's Sprites Git\LT．／LCDR．Hinamori Amu's Sprites - Z9S Resources"
    output_dir = r"D:\제1작업실\LT．／LCDR．Hinamori Amu's Sprites Git"
    
    # 출력 폴더가 존재하지 않는 경우 생성
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # 소스 폴더 내의 모든 파일 탐색 및 .Z9S 파일 처리
    if os.path.exists(source_dir):
        files = os.listdir(source_dir)
        z9s_files = [f for f in files if f.lower().endswith('.z9s')]
        
        if not z9s_files:
            print(f"'{source_dir}' 폴더 내에 .Z9S 파일이 존재하지 않습니다.")
        else:
            print(f"총 {len(z9s_files)}개의 .Z9S 파일을 찾았습니다. 추출을 시작합니다.")
            for file_name in z9s_files:
                full_file_path = os.path.join(source_dir, file_name)
                print(f"\n[대상 파일] {file_name} 처리 중...")
                extract_png_from_z9s(full_file_path, output_dir)
            print("\n모든 작업이 완료되었습니다.")
    else:
        print(f"소스 폴더 경로를 찾을 수 없습니다: {source_dir}")