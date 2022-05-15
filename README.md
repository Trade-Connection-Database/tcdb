# tcdb
## Русский
TCDB (trade connection database) - база данных торговых связей между компаниями, фондами и людьми. 
В данный момент база находится в стадии разработки, но вот как я вижу её развитие.
#### Концепция
DIY торговая блокада помогла сторонникам Ганди освободить свою страну ненасильственно, однако современный рынок устроен несколько сложнее чем в те времена, поэтому устроить DIY торговую блокаду Путину (или другому человеку творящему зверства) сложно.  
Эта база данных - инструмент чтобы осознанные люди могли финансово давить на людей творящих зверства по всему миру, не дожидаясь санкций от своей страны и обрезая опосредованные связи через страны, не вводившие санкций.  

#### Структура
 - веб-сервер написанный на fastapi и предоставляющий REST API на добавление и чтение данных
 - база данных, в которой хранятся все наши данные. В настоящий момент это postgresql
 - питоновская обёртка над API чтобы легко было читать и записывать данные программно
 - html/js клиент для удобного просмотра данных человеком
 
 #### Заполнение
 В первую очередь мы пойдём парсить данные с нефтяных бирж чтобы увидеть куда идёт нефть, однако есть множество других открытых данных из которых можно достать немало торговых связей, например  
  - финотчётность компаний
  - пресс-релизы, статьи новостных изданий
  - различные сливы, архив Пандоры например
  
Источников данных и методов их сборки может быть множество, поэтому мы и делаем API, чтобы сторонние неравнодушные разработчики могли добавлять данные, в хорошем варианте развития событий это станет основным источником наших данных.  
#### Использование
Когда наберётся достаточно данных база может быть использована журналистами новостных изданий, блогерами и просто интересующимися людьми чтобы понять, какие товары лучше не покупать чтобы мир был более в порядке.  
#### Контакты
oleg.demianchenko@gmail.com  
telegram: @oleg_demianchenko  

Любая помощь приетствуется.  
Если вы читаете это, вы и есть сопротивление, вместе хорошие люди победят.  
## English
TCDB (trade connection database) - databese of trade connections between companies, foundations and people.
At the moment the project is in the development stage, but that's how I see it in future
#### Concept
DIY trade embargo helped Ghandi and his followers to liberate their country without violence, but nowdays the market is much more complex than it used to be, so you can't make a DIY trade embargo on Putin (or any other person that is doing something alike).  
TCDB is a tool for concious people to create financial pressure on people doing something bad without waiting for oficial trade embargo from their government and cutting off indirect connections via the countries that didn't join to embargo.  

#### Structure
 - web-server on fastapi with REST API for reading and adding data.
 - database itself. At the moment it is postgresql
 - python wrapper on API so that data could be easile accessed and added programmatically
 - html/js client for convenient data representation for humans.

#### Data sources
First of all we are going to parse oil stock data, but there is lots of potential sources
 - finantial reports of companies
 - press-releases, newspaper articles
 - Various data leaks like Pandora archieve
 
Data sources and methods of their handling are very diverse, that's why we are creating API for data submission, we hope that volunteers all over the world will help us in data mining.  
#### Usage
When we will have enough data the databse can be used by news media, blogers and just people wondering what goods are better not to be bougt so that the world could be more okay.  
#### Contacts
oleg.demianchenko@gmail.com  
telegram: @oleg_demianchenko  


Any assistance is welcome.  
If you are reading this, you are the resistance, together the good people will be victorious.  
