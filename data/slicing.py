from sahi.slicing import slice_coco

def slicing(): 
    
    slice_coco(
        coco_annotation_file_path='annotations_path',
        image_dir='images_path',
        slice_height=640,
        slice_width=640,
        overlap_height_ratio=0.1,
        overlap_width_ratio=0.1,
        ignore_negative_samples=True,
    )