


# Contributing to Free Course Hive ( Backend )

  First off, thank you for considering contributing to **Free Course Hive!** Your involvement helps make this project better for everyone, whether it's by improving code, adding new features, fixing bugs, or improving documentation. 
  This guide will help you get started.


## How Can You Contribute?

  There are several ways to contribute to Free Course Hive:

  - Report a Bug: Found something that isn't working right? Open an issue and provide as much detail as possible.
    
  - Fix Bugs: Check the issues for any bugs and help fix them.
    
  - Improve the Code: Whether it's optimizing performance or refactoring code, your improvements are welcome.
    
  - Add Features: Have a cool feature in mind? Let's discuss it and implement it together!
    
  - Improve Documentation: If you find anything missing or unclear, feel free to suggest improvements or add more documentation.
    
  - Scrapers: Suggest or add more scrapers to pull data from new free course providers.
    

## Getting Started

  1. Fork the Repository
     
     To contribute, you'll first need to fork the repository:
     
       - Navigate to the main repository: Free Course Hive Backend
         
       - Click the Fork button (top right).


  2. Clone Your Fork

     After forking, clone your fork to your local machine:

       ```
       git clone https://github.com/yourusername/freecoursehive-backend.git
       cd freecoursehive-backend
       ```

  3. Set Up the Project

     Ensure you have Python and Flask installed. Follow the steps in the README.md to set up the backend and dependencies.

       - Create a virtual environment:
         
         ```
         python3 -m venv venv
         source venv/bin/activate  # On Windows: venv\Scripts\activate
         ```

     - Install dependencies:

       ```
       pip install -r requirements.txt

       ```


  4. Create a Branch
     
     Always work in a branch when contributing. Create a new branch for your feature or bugfix:

     ```
     git checkout -b your-feature-branch

     ```


  5. Make Your Changes

     Now it's time to make your changes! Whether you're fixing a bug, adding a feature, or improving documentation, feel free to dive into the code.


  6. Test Your Changes

     Make sure your changes work as expected and that they don’t break anything:

       - Run the Flask app locally:

         ```
         python app.py

         ```

       - Navigate to `http://127.0.0.1:5000/api/courses` and test the API.
         
    
  7. Commit Your Changes

      Once you are satisfied with your changes, commit them:

     ```
     git add .
     git commit -m "Description of your changes"
     ```

  8. Push Your Changes

     Push the changes to your forked repository:

     ```
     git push origin your-feature-branch

     ```
     

  9. Submit a Pull Request (PR)

      Go to the original repository and you should see a button to create a Pull Request (PR).
      Click on it and submit your PR, making sure to provide a detailed description of your changes.


      - Link any issues that the PR addresses by including a keyword like "Closes #issue-number".
      - Wait for a review and discussion, if necessary.


## Code Style

  To maintain consistency across the project, please follow these guidelines:

  - Follow PEP8 for Python code.
  - Write clear and concise commit messages.
  - Add comments where necessary to explain your code, especially for complex logic.
  - Keep PRs small and focused to make reviewing easier.



## Need Help?

  If you need any help while contributing, feel free to open an issue or ask in the discussion section of the repository. We're here to help!



Thank you again for contributing! Your efforts make **Free Course Hive** a better place for learners around the world.

    








