# A script for generating an outline for notes on a leetcode question

# gets the question info to generate the outline
def GetQuestionInfo():
  question_category = input('What category is this question? (e.g. "Arrays and Hashing")')
  question_name = input('What is the name of this question? (e.g. "Two Sum")')
  question_number = input('What is the question number? (e.g. "1")')
  question_link = input('What is the link to the question? (e.g. "https://leetcode.com/questions/two-sum/")')
  question_date = input('What is the date? (e.g. "06/16/2003")')
  
  return {
    'question_category': question_category,
    'question_name': question_name,
    'question_number': question_number,
    'question_link': question_link,
    'question_date': question_date
  }

# gets the question template
def GetQuestionTemplate():
  # question_template
  with open('files/templates/Question Template.md', 'r') as f:
    question_template = f.read()
  f.close()
  
  return question_template

# gets the question header
def GetQuestionHeader():
  # question_header
  with open('files/templates/New File Template.md', 'r') as f:
    question_header = f.readline(1)
  f.close()
  
  return question_header

# get the indices of where to insert the next question and its header
def GetIndices(file_path):
  with open(file_path, 'r') as f:
    lines = f.readlines()
  f.close()
  
  for index, line in enumerate(lines):
    if line.startswith('- [ ]') or line.startswith('- [x]'):
      last_header_index = index
    elif line.startswith('---'):
      last_question_index = index
  
  last_header_index += 1
  last_question_index += 1
    
  return {
    'last_header_index': last_header_index,
    'last_question_index': last_question_index
  }
     
    
if __name__ == '__main__':
  question_info = GetQuestionInfo()
  question_template = GetQuestionTemplate()
  question_header = GetQuestionHeader()
  
  file_path = 'files/questions/' + question_info['question_category'] + '.md'
  indices = GetIndices(file_path)
  with open(file_path, 'r+') as f:
    lines = f.readlines()
    lines.insert(indices['last_header_index'], question_header)
    lines.insert(indices['last_question_index'], question_template)
    f.seek(0)
    f.writelines(lines)
  f.close()