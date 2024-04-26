# import os.path

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# # If modifying these scopes, delete the file token.json.
# SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]


# def main():
#   """Shows basic usage of the Drive v3 API.
#   Prints the names and ids of the first 10 files the user has access to.
#   """
#   creds = None
#   # The file token.json stores the user's access and refresh tokens, and is
#   # created automatically when the authorization flow completes for the first
#   # time.
#   if os.path.exists("token.json"):
#     creds = Credentials.from_authorized_user_file("token.json", SCOPES)
#   # If there are no (valid) credentials available, let the user log in.
#   if not creds or not creds.valid:
#     if creds and creds.expired and creds.refresh_token:
#       creds.refresh(Request())
#     else:
#       flow = InstalledAppFlow.from_client_secrets_file(
#           "client_secret_1091742458180-k25bclsueluik9hnqnrqb8q8dgugdhk2.apps.googleusercontent.com.json", SCOPES
#       )
#       creds = flow.run_local_server(port=0)
#     # Save the credentials for the next run
#     with open("token.json", "w") as token:
#       token.write(creds.to_json())

#   try:
#     service = build("drive", "v3", credentials=creds)

#     # Call the Drive v3 API
#     results = (
#         service.files()
#         .list(pageSize=10, fields="nextPageToken, files(id, name)")
#         .execute()
#     )
#     items = results.get("files", [])

#     if not items:
#       print("No files found.")
#       return
#     print("Files:")
#     for item in items:
#       print(f"{item['name']} ({item['id']})")
#   except HttpError as error:
#     # TODO(developer) - Handle errors from drive API.
#     print(f"An error occurred: {error}")


# if __name__ == "__main__":
#   main()


























import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

def create_folder(service, folder_name):
    folder_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    folder = service.files().create(body=folder_metadata, fields='id').execute()
    return folder['id']

def upload_file(service, file_path, folder_id):
    media = MediaFileUpload(file_path)
    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [folder_id]
    }
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return file['id']

def main():
    """Shows basic usage of the Drive v3 API.
    Creates a folder, then uploads files to that folder.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens and is created
    # automatically when the authorization flow completes for the first time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secret_1091742458180-k25bclsueluik9hnqnrqb8q8dgugdhk2.apps.googleusercontent.com.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("drive", "v3", credentials=creds)

        # Create a folder
        folder_name = "test_feb9"
        folder_id = create_folder(service, folder_name)
        print(f"Folder '{folder_name}' created with ID: {folder_id}")

        # Upload files to the folder
        file_paths = ["text_files/test.txt", "text_files/jtjp.txt"]  # Add the paths of the files you want to upload
        for file_path in file_paths:
            file_id = upload_file(service, file_path, folder_id)
            print(f"File '{os.path.basename(file_path)}' uploaded with ID: {file_id}")

    except HttpError as error:
        # Handle errors from the Drive API.
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
