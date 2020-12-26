from pgdrive.scene_creator.algorithm.BIG import BIG
from pgdrive.scene_creator.road.road_network import RoadNetwork
from pgdrive.tests.block_test.test_block_base import TestBlock
from pgdrive.utils.asset_loader import AssetLoader
from panda3d.core import loadPrcFileData
from pgdrive.scene_creator.blocks.block import Block
from time import time


def vis_big(debug: bool = False, asset_path=None, block_num=40, lane_width=3.5, lane_num=2, seed=888,
            lane_line_width=1.0):
    start_time = time()
    Block.LANE_LINE_WIDTH = lane_line_width
    loadPrcFileData("", "win-size 1600, 900")
    if asset_path is not None:
        TestBlock.asset_path = asset_path
    test = TestBlock(debug=debug)

    test.setBackgroundColor(1, 1, 1, 1)
    test.setFrameRateMeter(False)

    test.cam.setPos(-200, -350, 2000)
    AssetLoader.init_loader(test, test.asset_path)
    test.graphicsEngine.renderFrame()
    test.graphicsEngine.renderFrame()
    test.graphicsEngine.renderFrame()
    test.graphicsEngine.renderFrame()
    test.graphicsEngine.renderFrame()
    while time() - start_time < 5:
        continue
    global_network = RoadNetwork()

    big = BIG(lane_num, lane_width, global_network, test.render, test.world, seed)
    test.vis_big(big)
    test.big.block_num = block_num
    # big.generate(BigGenerateMethod.BLOCK_NUM, 10)
    test.run()


if __name__ == "__main__":
    vis_big()
