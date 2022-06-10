from django.test import TestCase
from django.urls import reverse


from .models import Probe
from coder.coder import create_test_user


class ProbeDataTest(TestCase):

    def setUp(self):
        self.probe1 = dict(name='Shrinking World', page='https://Shrinking-World.com', text='Shrinking World')
        self.probe2 = dict(name='BACS 350', page='https://Shrinking-World.com/course/bacs350', text='Shrinking World')

    def test_add_probe(self):
        self.assertEqual(len(Probe.objects.all()), 0)
        Probe.create(**self.probe1)
        Probe.create(**self.probe2)
        x = Probe.objects.get(pk=2)
        self.assertEqual(str(x), 'BACS 350 - https://Shrinking-World.com/course/bacs350')
        self.assertEqual(x.page, 'https://Shrinking-World.com/course/bacs350')
        self.assertEqual(len(Probe.objects.all()), 2)

    def test_probe_edit(self):
        Probe.create(**self.probe1)
        b = Probe.objects.get(pk=1)
        b.page = self.probe2['page']
        b.text = self.probe2['text']
        b.save()
        self.assertEqual(b.page, self.probe2['page'])
        self.assertEqual(b.text, self.probe2['text'])

    def test_probe_delete(self):
        Probe.objects.create(**self.probe1)
        b = Probe.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Probe.objects.all()), 0)


class ProbeViewsTest(TestCase):

    def setUp(self):
        self.probe1 = dict(name='Shrinking World', page='https://Shrinking-World.com', text='Shrinking World')
        self.probe2 = dict(name='BACS 350', page='https://Shrinking-World.com/course/bacs350', text='Shrinking World')

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('probe_list'))

    def test_probe_list_view(self):
        self.assertEqual(reverse('probe_list'), '/probe/')
        Probe.objects.create(**self.probe1)
        Probe.objects.create(**self.probe2)
        response = self.client.get('/probe/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'probe_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_probe_detail_view(self):
        Probe.objects.create(**self.probe1)
        self.assertEqual(reverse('probe_detail', args='1'), '/probe/1')
        self.assertEqual(reverse('probe_detail', args='2'), '/probe/2')
        response = self.client.get(reverse('probe_detail', args='1'))
        self.assertContains(response, 'https://Shrinking-World.com')

    def test_probe_add_view(self):
        response = self.client.post(reverse('probe_add'), self.probe1)
        response = self.client.post(reverse('probe_add'), self.probe2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/probe/')
        response = self.client.get('/probe/')
        self.assertEqual(len(Probe.objects.all()), 2)
        response = self.client.get(reverse('probe_list'))
        self.assertContains(response, 'BACS 350')

    def test_probe_edit_view(self):
        Probe.objects.create(**self.probe1)
        self.client.post('/probe/1/', self.probe2)
        probe = Probe.objects.get(pk=1)
        self.assertEqual(probe.page, self.probe2['page'])

    def test_probe_delete_view(self):
        Probe.objects.create(**self.probe1)
        self.assertEqual(reverse('probe_delete', args='1'), '/probe/1/delete')
        response = self.client.post('/probe/1/delete')
        self.assertEqual(len(Probe.objects.all()), 0)
