import psutil
import pushbullet
battery_status = psutil.sensors_battery()

if battery_status.power_plugged:
    if battery_status.percent >= 80:
        pb = pushbullet.PushBullet('Replace this param with Your Token from Pushbullet')
        push = pb.push_note('Charging Complete!', f'Battery is {battery_status.percent}% Remove Charger!')
        print("Sent Notification to Phone.")
