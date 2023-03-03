from ctypes import windll
import win32api
import win32con
import time
import os
import pyperclip
import pyautogui as ui
from tqdm import tqdm

'''
1、遍历文件
2、复制文件
3、点击百度云客户端页面
4、模拟粘贴
'''
class AutoScreen:

    def __init__(self, height, width, path):
        self.height = height
        self.width = width
        self.path = path

    def __del__(self):
        # print("End")
        pass

    def get_info(self):
        # 将鼠标移动到目标位置
        windll.user32.SetCursorPos(self.height, self.width)
        # 鼠标左键按下
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.height, self.width)
        # time.sleep(0.05)
        # 鼠标左键释放
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.height, self.width)

    def click(self):
        self.get_info()

    def search_file(self):

        full_path_set = {}
        # 获取具体文件的路径
        for dirpath, dirnames, filenames in os.walk(self.path):
            if len(dirnames) == 0:
                full_path_set[dirpath] = filenames
            else:
                continue

        # 批量文件路径上传
        full_path_list = []
        bar2 = tqdm(total=len(full_path_set.keys()))
        for temp_path in full_path_set.keys():
            # 文件数量小于500时一次性全部上传
            if (len(full_path_set[temp_path])) < 500:

                # for i in range(4):
                #     # 点击刷新按钮
                #     auto2 = AutoScreen(height=337, width=124, path=self.path)
                #     auto2.click()
                #     time.sleep(1)

                # 点击上传按钮
                auto3 = AutoScreen(height=self.height, width=self.width, path=self.path)
                auto3.click()

                # 点击文件名跳转到指定目录
                pyperclip.copy(temp_path)
                time.sleep(0.5)
                ui.hotkey('ctrl', 'v')
                ui.press("enter")
                time.sleep(0.5)

                # 点击上传窗口区域
                auto3 = AutoScreen(height=500, width=400, path=self.path)
                auto3.click()
                time.sleep(0.5)
                ui.hotkey('ctrl', 'a')
                time.sleep(0.5)
                ui.press("enter")
                bar2.update()

            temp_path_str = ""
            temp_file_num = 0
            for filename in full_path_set[temp_path]:
                if (len(full_path_set[temp_path])) >= 500:
                    # 每次上传的数量
                    if temp_file_num >= 5:
                        full_path_list.append(temp_path_str)
                        temp_file_num = 0
                        temp_path_str = ""
                    else:
                        temp_file_num += 1
                        temp_path_str += '"' + temp_path + '\\' + filename + '"' + " "
                        continue

            full_path_list.append(temp_path_str)
        bar2.close()

        all_up_nums = len(full_path_list)
        current_up_nums = (all_up_nums // 10) * 7
        bar = tqdm(total=current_up_nums)

        # 上传
        ready_up_num = 0
        for batch_file_path in full_path_list:
            if ready_up_num < current_up_nums:
                print(batch_file_path)
                auto2 = AutoScreen(height=self.height, width=self.width, path=self.path)
                auto2.click()
                pyperclip.copy(batch_file_path)
                time.sleep(0.5)
                # pyperclip.paste()
                ui.hotkey('ctrl', 'v')
                ui.press("enter")
                bar.update()
                time.sleep(5)

                ready_up_num += 1

        bar.close()

    # 逐个上传
    def search_file2(self):

        full_path_list = []
        # 获取具体文件的路径
        for dirpath, dirnames, filenames in os.walk(self.path):
            for filename in filenames:
                if len(dirnames) == 0:
                    full_path_list.append(dirpath+'\\'+filename)
                else:
                    continue

        all_file_num = len(full_path_list)

        # 上传到百度云
        stop_num = (all_file_num // 10) * 10
        current_num = 0
        bar = tqdm(total=stop_num)
        print("总文件数:", all_file_num, "需要上传文件数:", stop_num)
        for temp_path in full_path_list:
            current_num += 1
            if current_num > stop_num:
                break
            else:
                auto2 = AutoScreen(height=self.height, width=self.width, path=self.path)
                auto2.click()
                pyperclip.copy(temp_path)
                # time.sleep(0.5)
                # pyperclip.paste()

                ui.hotkey('ctrl', 'v')
                ui.press("enter")
                bar.update()
                # time.sleep(0.5)

        bar.close()


if __name__ == '__main__':

    # 百度云客户端页面
    height = 300  # windll.user32.GetSystemMetrics(0)
    width = 70  # windll.user32.GetSystemMetrics(1)
    # path = "E:\\电子书\\EbookSearch\\【27】"
    # path = "E:\\电子书\\EbookSearch"

    # 注意目录的选择,选择当前目录中不含有需要上传的文件
    path = "E:\\电子书"

    auto = AutoScreen(height=height, width=width, path=path)
    # 警惕，不宜尝试
    # auto.click()
    # auto.search_file()
    auto.search_file2()
