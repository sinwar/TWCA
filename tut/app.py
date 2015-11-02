from rapidsms.apps.base import AppBase

class PingPong(AppBase):

    def handle(self, msg):
        if msg.text == 'ping':
            msg.respond('pong')
            return True	
        elif msg.text == '50 mo':
        	msg.respond('successful')
        	return True		
        '''elif msg.text == 'HELP':
        	msg.respond('send message in this way- Recharge Mobile no Your ID')
        	return True'''
        return False