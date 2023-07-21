# A script for generating an outline for notes on a leetcode question

import os
import git


# gets the question info to generate the outline
def getQuestionInfo():
  questionCategory = input('What category is this question? (e.g. "Arrays and Hashing")')
  questionName = input('What is the name of this question? (e.g. "Two Sum")')
  questionNumber = input('What is the question number? (e.g. "1")')
  questionLink = input('What is the link to the question? (e.g. "https://leetcode.com/questions/two-sum/")')
  dateSolved = input('What is the date? (e.g. "06/16/2003")')
  
  return {
    'questionCategory': questionCategory,
    'questionName': questionName,
    'questionNumber': questionNumber,
    'questionLink': questionLink,
    'dateSolved': dateSolved
  }

# gets the question template
def getQuestionTemplate():
  with open('files/templates/Question Template.md', 'r') as f:
    question_template = f.read()
  f.close()
  
  return question_template

# gets the question header
def getQuestionHeader():
  with open('files/templates/New File Template.md', 'r') as f:
    question_header = f.readline()
  f.close()
  
  return question_header

# gets the file template
def getFileTemplate():
  with open('files/templates/New File Template.md', 'r') as f:
    file_template = f.read()
    
  return file_template

# get the indices of where to insert the next question and its header
def getIndices(file_path):
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
  
# push the question to github
def beginCommitProcess(question_info):
  input('Press enter to push to github. Make sure you have filled in the template that was generated.')
  
  commit_message = question_info['questionName'] + ' (' + question_info['questionNumber'] + ')'
  repo = git.Repo(os.getcwd())
  repo.git.add('--all')
  repo.git.commit('-m', commit_message)
  repo.git.push()

     
# driver    
if __name__ == '__main__':
  question_info = getQuestionInfo()
  question_template = getQuestionTemplate()
  question_header = getQuestionHeader()
  
  file_path = 'files/questions/' + question_info['questionCategory'] + '.md'
  
  # if the file doesn't exist, create it
  new_file = False
  if not os.path.exists(file_path):
    new_file = True
    file_template = getFileTemplate()
    with open(file_path, 'w') as f:
      f.write(file_template)
    f.close()
    
  indices = getIndices(file_path)
  with open(file_path, 'r+') as f:
    updated_lines = f.readlines()
    
    # insert the question header and template
    if not new_file:
      updated_lines.insert(indices['last_header_index'], question_header)
      updated_lines.insert(indices['last_question_index'], question_template)
    
    # replace the question info in the template
    for info in question_info:
      updated_lines = [line.replace(info, str(question_info[info])) for line in updated_lines]

    f.seek(0)
    f.writelines(updated_lines)
  f.close()

  beginCommitProcess(question_info)
  
  
  
  
