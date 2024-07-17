import ModuleUpdate
import Utils
from worlds.khbbs.Client import launch
ModuleUpdate.update()

if __name__ == '__main__':
    Utils.init_logging("KHBBSClient", exception_logger="Client")
    launch()
