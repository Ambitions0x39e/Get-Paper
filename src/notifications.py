class NotificationDelegate(NSObject): # Class for Notification Present
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
