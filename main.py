import os
from moviepy import VideoFileClip


def convert_videos_to_mp3(input_folder, output_folder):
    # 如果输出文件夹不存在则创建
    os.makedirs(output_folder, exist_ok=True)

    # 遍历输入文件夹中的文件
    for filename in os.listdir(input_folder):
        # 检查扩展名
        if filename.lower().endswith((".mp4", ".mv")):
            input_path = os.path.join(input_folder, filename)
            # 去除原始扩展名，替换为 .mp3
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, base_name + ".mp3")

            print(f"正在处理: {input_path}")
            try:
                # 读取视频并提取音频
                clip = VideoFileClip(input_path)
                clip.audio.write_audiofile(output_path)
                clip.close()
                print(f"已输出: {output_path}")
            except Exception as e:
                print(f"转换失败 {filename} ：{e}")


if __name__ == "__main__":
    # 在这里替换为你的输入输出文件夹路径
    input_dir = r"你的输入文件夹路径"
    output_dir = r"你的输出文件夹路径"

    convert_videos_to_mp3(input_dir, output_dir)