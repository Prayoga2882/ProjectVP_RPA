from helper.index import *


def entrypoint():
    telkomsel_core()
    messagebox.showinfo("Proses Selesai", "Proses telah selesai.")
    # axis_core()


if __name__ == '__main__':
    entrypoint()
