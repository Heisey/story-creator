
import glob
import os
import utils
import jobs


output_dir = "src/models/flan_t5_comic" 

def main():
    utils.downloadModel("mosaicml/mpt-7b-storywriter")
  # test_prompt = "Create a comic book panel with: Setting: A dark forest at night, Character Action: A child cautiously walking with a flashlight, Dialogue: 'I hope I find it soon...', Narration: 'The forest was full of mysteries waiting to be uncovered.'"
  # result = jobs.generatePanel(test_prompt)
  # print(f'result {result}')


if __name__ == "__main__":
    main()
