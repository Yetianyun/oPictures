#分割图片
from PIL import Image

def cut_image(image,count):
    width, height = image.size
    item_width = int(width / count) 
    item_height = int(height / count)
    box_list = []
    # (left, upper, right, lower)
    for i in range(0,count):
        for j in range(0,count):
            box = (j*item_width,i*item_height,(j+1)*item_width,(i+1)*item_height)
            box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    return image_list

#保存
def save_images(image_list):
    index = 1
    for image in image_list:
        image.save(str(index) + '.png', 'PNG')
        index += 1

if __name__ == '__main__':
    file_path = "./sourceImages/WX20191218-224733.png"  #图片保存的地址
    image = Image.open(file_path)

    image_list = cut_image(image,2)
    save_images(image_list)