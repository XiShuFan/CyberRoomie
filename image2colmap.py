import os

# Feedforward prediction only
# os.system("python vggt/demo_colmap.py --scene_dir=scene_dir")

# With bundle adjustment
# --use_ba --fine_tracking
os.system("python vggt/demo_colmap.py --scene_dir=/media/why/新加卷/xsf/商品3DGS/scene")

# Run with bundle adjustment using reduced parameters for faster processing
# Reduces max_query_pts from 4096 (default) to 2048 and query_frame_num from 8 (default) to 5
# Trade-off: Faster execution but potentially less robust reconstruction in complex scenes (you may consider setting query_frame_num equal to your total number of images) 
# See demo_colmap.py for additional bundle adjustment configuration options
# TODO os.system("python vggt/demo_colmap.py --scene_dir=scene_dir --use_ba --max_query_pts=2048 --query_frame_num=5")