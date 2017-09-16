from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

class WebForm(Form):
	src1 = TextField('Location 1:')
	src2 = TextField('Location 2:')

	def reset(self):
		blankData = MultiDict([ ('csrf', self.reset_csrf())])
		self.process(blankData)