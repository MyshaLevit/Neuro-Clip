from moviepy.editor import VideoFileClip

def trim_video(filename, start_time, end_time):
    # Загружаем видеофайл с помощью MoviePy
    video_clip = VideoFileClip(filename)

    # Обрезаем видеофайл
    trimmed_clip = video_clip.subclip(start_time, end_time)

    # Генерируем имя выходного файла
    output_filename = f"trimmed_{start_time}_{end_time}.mp4"

    # Сохраняем обрезанный видеофайл
    trimmed_clip.write_videofile(output_filename, codec="libx264", audio_codec="aac")

    # Очищаем ресурсы
    video_clip.close()
    trimmed_clip.close()

    return output_filename