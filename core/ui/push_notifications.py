import logging
import subprocess
from .base import UI
from desktop_notifier import Button, DesktopNotifier, ReplyField
import asyncio

log = logging.getLogger(__name__)
notifier = DesktopNotifier()

class DarwinPushNotificationsUI(UI):
    async def message(self, message: str):
        subprocess.run(['osascript', '-e', f'display notification "{message}" with title "Local AI Utils"'])

    async def prompt(self, message: str):
        result = subprocess.run(['osascript', '-e', f'''
set dialogueReply to display dialog "{message}" default answer ""
return text returned of dialogueReply
        '''],
          capture_output=True,
          text=True
        )

        return result.stdout.strip()
    
    async def confirm(self, message: str):
        yes = 'Confirm'
        no = 'Abort'
        result = subprocess.run(['osascript', '-e', f'''
            set alertReply to display alert "Local AI Utils" message "{message}" buttons ["{yes}", "{no}"] default button 1
            if button returned of alertReply is "{yes}" then
                return true
            else
                return false
            end if
        '''],
          capture_output=True,
          text=True
        )

        return result.stdout.strip().lower() == 'true'
        

class PushNotificationsUI(UI):
    async def message(self, message: str):
      await notifier.send(title="Local AI Utils", message=message)

    async def prompt(self, message: str):
      loop = asyncio.get_event_loop()
      future = loop.create_future()

      def on_replied_callback(text: str):
        if not future.done():
          loop.call_soon_threadsafe(future.set_result, text)

      await notifier.send(
        title="Local AI Utils",
        message=message,
        reply_field=ReplyField(
            on_replied=on_replied_callback,
        )
      )

      return await future
    
    async def confirm(self, message: str):
      loop = asyncio.get_event_loop()
      future = loop.create_future()
      
      def on_pressed_callback(value: bool):
        if not future.done():
          loop.call_soon_threadsafe(future.set_result, value)

      await notifier.send(
        title="Local AI Utils",
        message=message,
        buttons=[
           Button(
              title="Confirm",
              on_pressed=lambda: on_pressed_callback(True)
           ),
           Button(
              title="Abort",
              on_pressed=lambda: on_pressed_callback(False)
           )
        ]
      )

      return await future