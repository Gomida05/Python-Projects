from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from typing import List, Union
from os import path, makedirs, listdir


class ConvertMp4ToMp3:
    def __init__(self, src: Union[List[str], str], dest: str):
        """
        Convert mp4 file to mp3 file
            :param src: str or list[str] the source file or directory
            :param dest: str the destination directory
            :raises TypeError: if src is not str or list[str]
            :raises Exception: if there is an error in the conversion process
            :raises Exception: if the source is not a file or directory
        """
        if isinstance(src, list):
            self.isList = True
        elif isinstance(src, str):
            self.isList = False
        else:
            raise TypeError("Currently this class only accept list[str] or str")
        self.src = src
        self.dest = dest



    def convert_mp4_to_mp3(self):
        """
        Convert mp4 file to mp3 file only single file
            :param src: str the source file
            :param dest: str the destination directory
            :raises Exception: if there is an error in the conversion process
            :raises Exception: if the source is not a file or directory
        """
        if path.isfile(self.src):
            self.__isTheDirectoryExits()
            try:
                videoFile= VideoFileClip(self.src)
                
                with videoFile.audio as videoFileToAudio:
                    if (videoFileToAudio is not None):
                        videoFileToAudio.write_audiofile(self.__replaceMp4ToMp3(self.src))
                        videoFileToAudio.close()
                        print("Video file converted to audio file successfully")
                    else:
                        raise Exception("There is no audio in the video file")

            except KeyError:
                audioFile= AudioFileClip(self.src)
                audioFile.write_audiofile(self.__replaceMp4ToMp3(self.src))
            except Exception as e:
                raise Exception(f"there is an error {e}")
        elif path.isdir(self.src):
            self.convert_mp4s_to_mp3s()
        else:
            raise Exception("The source is not a file or directory")

    def convert_mp4s_to_mp3s(self):
        """
        Convert mp4 file to mp3 file only for multiple files
            :param src: str the source file
            :param dest: str the destination directory
            :raises Exception: if there is an error in the conversion process
            :raises Exception: if the source is not a file or directory
        """
        if path.isfile(self.src):
            self.convert_mp4_to_mp3()
        if path.isdir(self.src):
            self.__isTheDirectoryExits()
            source = self.__give_me_list()
            for i in source:
                print(f"Processing file: {i}")
                try:
                    change = VideoFileClip(i)
                
                    with change.audio as videoFileToAudio:
                        if (videoFileToAudio is not None):
                            videoFileToAudio.write_audiofile(self.__replaceMp4ToMp3(i))
                            videoFileToAudio.close()
                        else:
                            print(f"Skipping {i}: No audio track found.")
                            continue
                    
                except Exception as e:
                    raise Exception(f"Error processing {i}: {e}")
        else:
            raise Exception("The source is not a file or directory")

    def __isTheDirectoryExits(self)-> bool:
        try:
            if path.exists(self.dest):
                return True
            else:
                makedirs(self.dest)
                return True
        except Exception as e:
            raise Exception(f"there is an error {e}")
        
    def __replaceMp4ToMp3(self, file_path: str) -> str:
        file_name = path.basename(file_path).replace(".mp4", ".mp3")
        return path.join(self.dest, file_name)

    def __give_me_list(self) -> List[str]:
        newList = []
        for i in listdir(self.src):
            # Get the file extension
            file_extension = path.splitext(i)[1]
            # Check if the file is an .mp4 file
            if file_extension == ".mp4":
                newList.append(path.join(self.src, i))
        return newList

