import time
import win10toast

def sendAlert():
    alert = win10toast.ToastNotifier()
    alert.show_toast("Alert Test!!!", "Alert Content is here")

    while alert.notification_active():
        time.sleep(1)


if __name__ == '__main__':
    sendAlert()
