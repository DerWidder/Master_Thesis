# _*_ coding: utf-8 _*_
import regex as re

def change_path_with_RegEx(file_path, src, new_file, target_path, org_path):
    """

    :param file_path: the file which contains the paths need to be changed
    :param src: search path part, here SA_CameraSetup: r"SA_CameraSetup", must add r before string
    :param target_path: the front of the searched path to be changed into
        r"\\\\\\\\data\\\\scratch_nobackup\\\\Postfächer\\\\fischer\\\\_StudentischeArbeiten\\\\MT_YZ\\\\NX12\\\\SA_CameraSetup"
    :param new_file: create a new file to contain the processed paths
    :param org_path: the front of the original path to be processed
        r"\\\\\\\\data\\\\projekte\\\\2019_Grace2\\\\Pruefstand\\\\CAD\\\\NX\\\\A_TestBench\\\\B_TestBench\\\\SA\\\\SA_CameraSetup"
        the regex form: r"\\\\\\\\data\\\\\w+\\\\\w+\\\\\w+\\\\\w+\\\\\w+\\\\\w+\\\\\w+\\\\SA\\\\SA_CameraSetup"
    :return: no return, only create a new file
    one thing to focus is that, the file_name will also be written in the file, remember to delete it.
    """

    with open(file_path, "r+", encoding="utf-8") as f:  # open the original file
        with open(new_file, "w+", encoding="utf-8") as f1:  # create the new file
            for i in f:
                if re.search(src, i):  # search for the path which contains the target
                    print(i)  # show the original path
                    res = re.sub(
                        org_path,
                        target_path, i)
                    print(res)  # show the processed path
                else:
                    res = i

                f1.write(res)
                # if only want CameraSetup, no need to use /else/. Just write res and keep rests out
                # one more thing to focus is that, the file_name will also be written in the file, remember to delete it.

if __name__ == '__main__':
    change_path_with_RegEx("load_options_B.def", r"SA_CameraSetup", "load_options_B_processed.def",
                           r"\\\\\\\\data\\\\scratch_nobackup\\\\Postfächer\\\\fischer\\\\_StudentischeArbeiten\\\\MT_YZ\\\\NX12\\\\SA_CameraSetup",
                           r"\\\\\\\\data\\\\\w+\\\\\w+\\\\\w+\\\\\w+\\\\\w+\\\\\w+\\\\\w+\\\\SA\\\\SA_CameraSetup")