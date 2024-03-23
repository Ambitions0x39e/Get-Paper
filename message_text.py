import objc
from Cocoa import NSObject
from AppKit import NSUserNotificationCenter, NSUserNotification

class NotificationDelegate(NSObject):
    def userNotificationCenter_didActivateNotification_(self, center, notification):
        # Handle notification activation
        pass

def send_notification(title, subtitle, message):
    delegate = NotificationDelegate.alloc().init()
    center = NSUserNotificationCenter.defaultUserNotificationCenter()
    center.setDelegate_(delegate)

    notification = NSUserNotification.alloc().init()
    notification.setTitle_(title)
    notification.setSubtitle_(subtitle)
    notification.setInformativeText_(message)

    center.deliverNotification_(notification)

if __name__ == "__main__":
    send_notification("Hello", "Python Notification", "This is a test notification from Python.")
