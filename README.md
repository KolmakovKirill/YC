Ссылка на сервис: http://158.160.3.27:8000/

Сервис развернут на Яндекс.Облако 

  Хранилище: Бакет Yandex Object Storage. В нем хранятся стили для элементов веб-сервиса

  БД: кластер Yandex Managed PostgreSQL
  
  IAM: Два сервисных аккаунта для YOS и тераформом (static-uploader и terraform-sa). Для них назначены роли storage.editor и др
  
  Сеть: VPC и подсеть в зоне ru-central1-a
