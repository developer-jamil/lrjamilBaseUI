import os

def generate_xml(scale, folder, filename):
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, filename), 'w') as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n')
        f.write('    <!-- Text Sizes (Scaled) -->\n')
        f.write(f'    <dimen name="normal_t_size">{int(15*scale)}sp</dimen>\n')
        f.write(f'    <dimen name="small_t_size">{int(12*scale)}sp</dimen>\n')
        f.write(f'    <dimen name="smallest_t_size">{int(11*scale)}sp</dimen>\n')
        f.write(f'    <dimen name="text_view_medium_t_size">{int(14*scale)}sp</dimen>\n')
        f.write(f'    <dimen name="header_1_t_size">{int(18*scale)}sp</dimen>\n')
        f.write(f'    <dimen name="header_2_t_size">{int(24*scale)}sp</dimen>\n')
        f.write(f'    <dimen name="header_3_t_size">{int(25*scale)}sp</dimen>\n\n')
        
        f.write(f'    <!-- Positive SDP values 1-500 (Scaled by {scale}) -->\n')
        for i in range(1, 501):
            val = f"{i*scale:.2f}dp"
            f.write(f'    <dimen name="_{i}sdp">{val}</dimen>\n')
            
        f.write('\n    <!-- Negative SDP values 1-500 -->\n')
        for i in range(1, 501):
            val = f"{-i*scale:.2f}dp"
            f.write(f'    <dimen name="_minus{i}sdp">{val}</dimen>\n')
            
        f.write('</resources>')

base_path = r"C:\Users\jamil\AndroidStudioProjects\JamilBaseUI\scalable-dimen\src\main\res"

# sw600dp (7" Tablet) ~ 1.3x scale
generate_xml(1.3, os.path.join(base_path, 'values-sw600dp'), 'dimens.xml')
# sw720dp (10" Tablet) ~ 1.5x scale
generate_xml(1.5, os.path.join(base_path, 'values-sw720dp'), 'dimens.xml')

print("Dimensions generated successfully!")
