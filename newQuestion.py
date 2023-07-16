# A script for generating an outline for notes on a leetcode question

# gets the question info to generate the outline
def GetQuestionInfo():
  # questionCategory = input('What category is this question? (e.g. "Arrays and Hashing")')
  # questionName = input('What is the name of this question? (e.g. "Two Sum")')
  # questionNumber = input('What is the question number? (e.g. "1")')
  # questionLink = input('What is the link to the question? (e.g. "https://leetcode.com/questions/two-sum/")')
  # dateSolved = input('What is the date? (e.g. "06/16/2003")')
  
  questionCategory = 'Stack'
  questionName = 'Test'
  questionNumber = 56
  questionLink = 'https://leetcode.com/problems/merge-intervals/'
  dateSolved = '06/16/2003'
  
  return {
    'questionCategory': questionCategory,
    'questionName': questionName,
    'questionNumber': questionNumber,
    'questionLink': questionLink,
    'dateSolved': dateSolved
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
    question_header = f.readline()
  f.close()
  
  print(question_header)
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
  last_question_index += 2
    
  return {
    'last_header_index': last_header_index,
    'last_question_index': last_question_index
  }
     
    
if __name__ == '__main__':
  question_info = GetQuestionInfo()
  question_template = GetQuestionTemplate()
  question_header = GetQuestionHeader()
  
  file_path = 'files/questions/' + question_info['questionCategory'] + '.md'
  indices = GetIndices(file_path)
  with open(file_path, 'r+') as f:
    updated_lines = f.readlines()
    
    # insert the question header and template
    updated_lines.insert(indices['last_header_index'], question_header)
    updated_lines.insert(indices['last_question_index'], question_template)
    
    # replace the question info in the template
    for info in question_info:
      updated_lines = [line.replace(info, str(question_info[info])) for line in updated_lines]
    
    # updated_lines = [line.replace('questionName', question_info["questionName"]) for line in lines]
    # updated_lines = [line.replace('questionNumber', str(question_info["questionNumber"])) for line in updated_lines]
    # updated_lines = [line.replace('questionLink', question_info["questionLink"]) for line in updated_lines]
    # updated_lines = [line.replace('dateSolved', question_info["dateSolved"]) for line in updated_lines]
    # updated_lines = [line.replace('questionCategory', question_info["questionCategory"]) for line in updated_lines]

    f.seek(0)
    f.writelines(updated_lines)
  f.close()