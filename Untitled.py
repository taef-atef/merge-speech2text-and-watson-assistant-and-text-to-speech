#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install ibm_watson


# In[2]:


pip install ibm_cloud_sdk_core


# In[3]:


from ibm_watson import TextToSpeechV1


# In[4]:


from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# In[5]:


api=IAMAuthenticator('oL2eTpIINazjXif2BR8p4oFNEJH3oN3E-bnPIawKoOEY')


# In[6]:


txt2speech=TextToSpeechV1(authenticator=api)


# In[7]:


txt2speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/ad036d83-ffdc-439d-8651-89378f516445')


# In[11]:


with open("speech.mp3","wb") as audiofile:
    audiofile.write(
        txt2speech.synthesize("Hello, this is python and IBM homework it was really amazing coding with this features"
                              ,accept="audio/mp3").get_result().content
    )


# # speech to text

# In[12]:


from ibm_watson import SpeechToTextV1


# In[13]:


api='qpombChgxcJkXTbFEKh-ulPDGesRGQ2G_nTVOBSEYnz7'
url='https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/4f149214-b1dd-44b6-9174-6e60504ae6fc'


# In[14]:


api=IAMAuthenticator(api)


# In[15]:


s2t=SpeechToTextV1(authenticator=api)


# In[16]:


s2t.set_service_url(url)


# In[18]:


with open('speech.mp3','rb') as f:
    res=s2t.recognize(audio=f,content_type='audio/mp3',model='en-US_NarrowbandModel',continous=True).get_result()


# In[20]:


text=res['results'][0]['alternatives'][0]['transcript']


# In[21]:


text


# In[22]:


with open('output.txt','w') as out:
    out.writelines(text)


# In[ ]:




