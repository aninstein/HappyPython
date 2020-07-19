#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os

from multiprocessing import Pool


BASE_DIR = os.getcwd()
ACTOR_LIST = os.path.join(BASE_DIR, "actor_list")
VIDEO_LIST = os.path.join(BASE_DIR, "videos")
SUPPORT_DESIGNATION = ["ssni", "snis", "ipx", "mide"]


def read_actor_list():
    actor_list_file = os.listdir(ACTOR_LIST)
    ret_data = {}
    for file_name in actor_list_file:
        video_list = []
        file_path = os.path.join(ACTOR_LIST, file_name)
        with open(file_path) as f:
            for row in f:
                video_list.append(row.strip().lower())
        actor_name = str(file_name)[:-4]
        ret_data[actor_name] = list(set(video_list))
    return ret_data


def create_video_dir(actor_list):
    ret_data = {}
    try:
        for actor, video_list in actor_list.items():
            act_video_dir = os.path.join(VIDEO_LIST, actor)
            if not os.path.exists(act_video_dir):
                os.makedirs(act_video_dir)
            video_map = {}
            for video in video_list:
                video_url = get_video_url(video)
                if video_url:
                    video_map[video] = video_url
            ret_data[act_video_dir] = video_map
        return ret_data
    except Exception as e:
        import traceback
        traceback.format_exc()
        print(e)
    return []


def get_video_url(designation):
    desig = designation.split("-")
    desig_conpany = desig[0]
    if desig_conpany not in SUPPORT_DESIGNATION:
        return ""
    desig_number = desig[1]
    single_str = desig_conpany[0]
    three_str = desig_conpany[:3]
    full_str = "{0}00{1}".format(desig_conpany, desig_number)
    url = "https://cc3001.dmm.co.jp/litevideo/freepv/{0}/{1}/{2}/{2}_dmb_w.mp4".format(single_str, three_str, full_str)
    return url


def multiple_download_video(video_list):
    download = Pool(10)
    res_list = []
    for path, video_map in video_list.items():
        for number, url in video_map.items():
            video_name = "{0}\\\{1}.mp4".format(path, number)
            if os.path.isfile(video_name):
                continue
            print("input filename: %s, url: %s " % (video_name, url))
            res = download.apply_async(download_video, args=(video_name, url), callback=pasrse_page)
            res_list.append(res)
    download.close()
    download.join()
    print([res.get() for res in res_list])
    print("all video is download")


def download_video(video_path, url):
    try:
        video_file = requests.get(url)
        with open(video_path, "wb") as f:
            f.write(video_file.content)
    except Exception as e:
        import traceback
        traceback.format_exc()
        print(e)
    return {"url": url}


def pasrse_page(res):
    print('<进程> %s finish, url: %s' % (os.getpid(), res.get("url", "")))


if __name__ == "__main__":
    actor = read_actor_list()
    video_list = create_video_dir(actor)
    multiple_download_video(video_list)
