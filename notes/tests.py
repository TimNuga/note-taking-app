from django.test import TestCase
from .models import Note
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class NoteModelTest(TestCase):
    def setUp(self):
        Note.objects.create(content="Test Note")

    def test_note_creation(self):
        note = Note.objects.get(content="Test Note")
        self.assertEqual(note.content, "Test Note")

class NoteListTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('note-list')

    def test_create_note(self):
        data = {"content": "Test Note"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.get().content, "Test Note")

    def test_list_notes(self):
        Note.objects.create(content="Test Note 1")
        Note.objects.create(content="Test Note 2")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class NoteDetailTestCase(APITestCase):
    def setUp(self):
        self.note = Note.objects.create(content="Test Note")
        self.url = reverse('note-detail', kwargs={'pk': self.note.pk})

    def test_get_note(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], self.note.content)

    def test_update_note(self):
        data = {"content": "Updated Content"}
        response = self.client.put(self.url, data)
        self.note.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.note.content, "Updated Content")

    def test_delete_note(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Note.objects.count(), 0)

    def test_get_invalid_note(self):
        response = self.client.get(reverse('note-detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
