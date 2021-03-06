from pgdrive.scene_creator.blocks.curve import Curve
from pgdrive.scene_creator.blocks.ramp import InRampOnStraight, OutRampOnStraight
from pgdrive.scene_creator.blocks.roundabout import Roundabout
from pgdrive.scene_creator.blocks.small_curve import SmallCurve
from pgdrive.scene_creator.blocks.std_intersection import StdInterSection
from pgdrive.scene_creator.blocks.std_t_intersection import StdTInterSection
from pgdrive.scene_creator.blocks.straight import Straight


class PGBlock:
    TYPE = {
        Curve: 0,
        SmallCurve: 0.7,
        Straight: 0.1,
        StdInterSection: 0,
        Roundabout: 0,
        StdTInterSection: 0,
        InRampOnStraight: 0.1,
        OutRampOnStraight: 0.1
    }

    @classmethod
    def all_blocks(cls):
        ret = list(cls.TYPE.keys())
        return ret

    @classmethod
    def get_block(cls, block_id: str):
        for block in cls.all_blocks():
            if block.ID == block_id:
                return block
        raise ValueError("No {} block type".format(block_id))

    @classmethod
    def block_probability(cls):
        return list(cls.TYPE.values())
