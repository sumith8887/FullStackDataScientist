import os
from supabase import create_client, Client
from datetime import datetime
import sys

# Set your Supabase credentials here
url = "https://dfzcpdgakbisetrdhlbu.supabase.co"
key= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRmemNwZGdha2Jpc2V0cmRobGJ1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODIzODgsImV4cCI6MjA3MzY1ODM4OH0.HKKZXk3gQxW3flqAH9QpMuOsGUmVnGOjKv6VDSgBiL0"

supabase: Client = create_client(url, key)

def add_member():
    name = input("Member name: ")
    email = input("Member email: ")
    resp = supabase.table("members").insert({"name": name, "email": email}).execute()
    print(resp.data)

def add_book():
    title = input("Book title: ")
    author = input("Book author: ")
    category = input("Book category: ")
    stock = int(input("Stock quantity: "))
    resp = supabase.table("books").insert({
        "title": title, "author": author, "category": category, "stock": stock
    }).execute()
    print(resp.data)

def list_books():
    resp = supabase.table("books").select("*").execute()
    for book in resp.data:
        print(book)

def search_books():
    keyword = input("Search keyword: ")
    resp = supabase.table("books").select("*").or_(
        f"title.ilike.%{keyword}%,author.ilike.%{keyword}%,category.ilike.%{keyword}%"
    ).execute()
    for book in resp.data:
        print(book)

def show_member():
    member_id = int(input("Member ID: "))
    member = supabase.table("members").select("*").eq("member_id", member_id).execute().data[0]
    print(member)
    borrow_records = supabase.table("borrow_records").select("book_id, return_date, books(title)").eq("member_id", member_id).execute().data
    for br in borrow_records:
        status = "Returned" if br["return_date"] else "Not returned"
        print(f"Book ID: {br['book_id']}, Title: {br['books']['title']}, Status: {status}")

def update_book_stock():
    book_id = int(input("Book ID: "))
    stock = int(input("New stock: "))
    resp = supabase.table("books").update({"stock": stock}).eq("book_id", book_id).execute()
    print(resp.data)

def update_member_email():
    member_id = int(input("Member ID: "))
    email = input("New email: ")
    resp = supabase.table("members").update({"email": email}).eq("member_id", member_id).execute()
    print(resp.data)

def delete_member():
    member_id = int(input("Member ID to delete: "))
    supabase.table("members").delete().eq("member_id", member_id).execute()
    print("Member deleted.")

def delete_book():
    book_id = int(input("Book ID to delete: "))
    supabase.table("books").delete().eq("book_id", book_id).execute()
    print("Book deleted.")

def borrow_book():
    member_id = int(input("Member ID: "))
    book_id = int(input("Book ID: "))
    book = supabase.table("books").select("stock").eq("book_id", book_id).execute().data[0]
    if book["stock"] < 1:
        print("Book not available")
        return
    supabase.table("books").update({"stock": book["stock"] - 1}).eq("book_id", book_id).execute()
    supabase.table("borrow_records").insert({"member_id": member_id, "book_id": book_id}).execute()
    print("Book borrowed.")

def return_book():
    member_id = int(input("Member ID: "))
    book_id = int(input("Book ID: "))
    borrow = supabase.table("borrow_records").select("*").eq("member_id", member_id).eq("book_id", book_id).is_("return_date", None).execute().data[0]
    supabase.table("borrow_records").update({"return_date": datetime.utcnow().isoformat()}).eq("record_id", borrow["record_id"]).execute()
    book = supabase.table("books").select("stock").eq("book_id", book_id).execute().data[0]
    supabase.table("books").update({"stock": book["stock"] + 1}).eq("book_id", book_id).execute()
    print("Book returned.")

def main():
    while True:
        print("""
        1. Add Member
        2. Add Book
        3. List Books
        4. Search Books
        5. Show Member Details
        6. Update Book Stock
        7. Update Member Email
        8. Delete Member
        9. Delete Book
        10. Borrow Book
        11. Return Book
        12. Exit
        """)
        choice = input("Choose option: ")
        options = {
            "1": add_member,
            "2": add_book,
            "3": list_books,
            "4": search_books,
            "5": show_member,
            "6": update_book_stock,
            "7": update_member_email,
            "8": delete_member,
            "9": delete_book,
            "10": borrow_book,
            "11": return_book,
            "12": lambda: sys.exit(0)
        }
        if choice in options:
            options[choice]()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
