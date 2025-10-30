from typing import List


def _is_operator(token: str) -> bool:
	return token in {"+", "-", "*", "/", "^"}


def _precedence(op: str) -> int:
	# Higher number means higher precedence
	if op == '+' or op == '-':
		return 1
	if op == '*' or op == '/':
		return 2
	if op == '^':
		return 3
	return 0


def _associativity(op: str) -> str:
	# returns 'left' or 'right'
	if op == '^':
		return 'right'
	return 'left'


def _tokenize(expr: str) -> List[str]:
	tokens: List[str] = []
	current = ''
	for ch in expr:
		if ch.isspace():
			if current:
				tokens.append(current)
				current = ''
			continue
		if ch.isalnum() or ch == '.':
			current += ch
		else:
			if current:
				tokens.append(current)
				current = ''
			tokens.append(ch)
	if current:
		tokens.append(current)
	return tokens


def infix_to_postfix(expression: str) -> str:
	if not expression or expression.strip() == '':
		return ''

	output: List[str] = []
	stack: List[str] = []  # operator stack

	tokens = _tokenize(expression)

	for token in tokens:
		if token.isalnum() or token.replace('.', '', 1).isdigit():
			# operand (variable or number)
			output.append(token)
		elif _is_operator(token):
			while stack and _is_operator(stack[-1]):
				top = stack[-1]
				if (_associativity(token) == 'left' and _precedence(token) <= _precedence(top)) or (
					_associativity(token) == 'right' and _precedence(token) < _precedence(top)
				):
					output.append(stack.pop())
				else:
					break
			stack.append(token)
		elif token == '(':
			stack.append(token)
		elif token == ')':
			# pop until matching '('
			while stack and stack[-1] != '(':
				output.append(stack.pop())
			if stack and stack[-1] == '(':
				stack.pop()
			else:
				# mismatched parenthesis -- ignore for now
				pass
		else:
			# unknown token: treat as operand to be safe
			output.append(token)

	while stack:
		top = stack.pop()
		if top in ('(', ')'):
			continue
		output.append(top)

	return ' '.join(output)

