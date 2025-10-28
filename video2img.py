#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Version: 1.0
@Author: Mr.WenC
@File: video2img.py
@Time: 2025-10-13 10:48:00
@License: (C)Copyright 2020-2030, Mr.WenC
@Desc: 
"""
import os
import cv2
import argparse
from loguru import logger
from datetime import datetime


def video2img(video_path, save_path, fps=1):
    """
    将视频文件转换为图片文件
    :param video_path: 视频文件路径
    :param save_path: 图片保存路径
    :param fps: 图片帧率
    :return: None
    """
    if not os.path.exists(video_path):
        print("Error: video file not exists!")
        return
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            logger.info("Reached end of video or Failed to read the video.")
            break
        
        now = datetime.now()
        image_path = os.path.join(save_path, f"{now.strftime('%Y%m%d%H%M%S%f')}.jpg")
  
        if frame_count % fps == 0:
            cv2.imwrite(image_path, frame)
            logger.info(f"Save image: {image_path}")

        frame_count += 1
    else:
        logger.error("Video to image conversion failed!")
    cap.release()
    logger.info("Finished and Video to image conversion completed!, ")    

if __name__ == '__main__':      
    parser = argparse.ArgumentParser(description='Convert video to image')
    parser.add_argument('--video_path', type=str, help='video file path')
    parser.add_argument('--save_path', type=str, help='image save path')
    parser.add_argument('--fps', type=int, default=1, help='image frame rate')
    args = parser.parse_args()
    video2img(args.video_path, args.save_path, args.fps)

    