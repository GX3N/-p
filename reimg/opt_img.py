#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
from pathlib import Path
from PIL import Image
import sys

def convert_images_to_webp(base_folder):
    """이미지 파일을 WebP 형식으로 변환하고 원본 파일을 삭제합니다."""
    base_path = Path(base_folder)
    supported_extensions = {'.jpg', '.jpeg', '.png'}

    for img_path in base_path.rglob('*'):
        if img_path.suffix.lower() in supported_extensions:
            webp_path = img_path.with_suffix('.webp')
            try:
                with Image.open(img_path) as img:
                    img.save(webp_path, "webp")
                logging.info(f"변환 완료: {img_path} -> {webp_path}")
                img_path.unlink()
            except Exception as e:
                logging.error(f"오류 발생: {img_path} 변환 중 오류가 발생했습니다. {e}")

def main():
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    try:
        # 스크립트가 위치한 디렉토리를 base_folder로 설정
        script_dir = Path(__file__).parent.resolve()
        convert_images_to_webp(base_folder=script_dir)
    except Exception as e:
        logging.error(f"Error: 이미지 변환 중 오류 발생: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
