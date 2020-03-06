from cv2 import cv2


def game_images(number):
    if number == 1:
        start_image = cv2.imread('1.jpg')
        cv2.imshow('Start the Game', start_image)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
    elif number == 2:
        start_image = cv2.imread('2.jpg')
        cv2.imshow('Wrong Answer', start_image)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
    elif number == 3:
        start_image = cv2.imread('3.jpg')
        cv2.imshow('Wrong Answer', start_image)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
    elif number == 4:
        start_image = cv2.imread('4.jpg')
        cv2.imshow('Wrong Answer', start_image)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
    elif number == 5:
        start_image = cv2.imread('5.jpg')
        cv2.imshow('Wrong Answer', start_image)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
    elif number == 6:
        start_image = cv2.imread('6.jpg')
        cv2.imshow('Wrong Answer', start_image)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
    elif number == 7:
        start_image = cv2.imread('7.jpg')
        cv2.imshow('Game Over', start_image)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()


