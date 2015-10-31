from rapidsms.contrib.handlers import KeywordHandler

help_text = {
    'aaa': 'Help for aaa',
    'bbb': 'Help for bbb',
    'ccc': 'Help for ccc',
}


class HelpHandler(KeywordHandler):
    keyword = "help"

    def help(self):
        """Invoked if someone just sends `HELP`.  We also call this
        from `handle` if we don't recognize the arguments to HELP.
        """
        self.respond("Send SMS in this way- rech <RechargeVAlue> <mobile number> <username>")

    def handle(self, text):
        """Invoked if someone sends `HELP <any text>`"""
        text = text.strip().lower()
        if text == 'aaa':
            self.respond(help_text['aaa'])
        elif text == 'bbb':
            self.respond(help_text['bbb'])
        elif text == 'ccc':
            self.respond(help_text['ccc'])
        else:
            self.help()
'''class Recharge(KeywordHandler):
    keyword='rech'
    def help(self):
        self.respond("Please send the message again with the Recharge value and mobile number send help for more")
    def handle(self,text):
        if text='50':
            self.respond("%s"+help_text['50'])'''