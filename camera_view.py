from flask import Blueprint, render_template, Response

from camera_controller import ImageStorage
img_hub = ImageStorage()

bp = Blueprint('camera_view', __name__)


@bp.route('/view_camera/<cam_id')
def view_camera(cam_id):
    return render_template('camera_view.html', cam_id=cam_id)


@bp.route('/view_camera/<cam_id>/video_feed')
def video_feed(cam_id):
    return Response(gen(cam_id),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def gen(cam_id):
    while True:
        try:
            frame = img_hub.get_image_dict()[cam_id]
        except KeyError as ex:
            frame = b''

        yield (b'---frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@bp.route('/')
def index():
    cam_dict = img_hub.get_image_dict()
    cams = []
    for c in cam_dict:
        cams.append(c)

    return render_template('index.html', cameras=cams)
