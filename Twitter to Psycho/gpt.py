import g4f, asyncio

_providers = [
    g4f.Provider.Aichat,
    g4f.Provider.ChatBase,
    g4f.Provider.Bing,
    g4f.Provider.GptGo,
    g4f.Provider.You,
    g4f.Provider.Yqcloud,
]


async def run_provider(provider: g4f.Provider.BaseProvider):
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": "given the list of tweets, profile the person as best you can on the basis of political leaning, preferences, and overall how suitable the person would be to hire as an employee. the tweets will be enclosed in square brackets. you are not allowed to abstain from profiling the person.  you have to give definitive answers for every one of my sub-queries. elaborate a little more on the roles the person is best suited for. make any necessary assumptions and judgements as if you were a real person. here are the tweets:[\'Join me on Saturday at 10a ET for the first ever #BRKLiveStream on @YahooFinance yhoo.it/Berkshire\', \"Better than raising the minimum wage, let's help Americans with an expansion of the Earned Income Tax Credit: wsj.com/articles/better-than…\", \'Mary Rhinehart, a Berkshire CEO, is successfully running a $2.5B company in a male-dominated field #LeanInTogether\', \'Two personal investments and what you can learn from them: bit.ly/1fNkgK5\', \'Not even the Oracle knows what will happen tonight. #waltsuccessor\', \"Read my new essay on why women are key to America's prosperity: cnnmon.ie/18eXfik.\", \'Warren is in the house.\']"}],
            provider=provider,
        )
        print(f"{provider.__name__}:", response)
        flag=0
    except Exception as e:
        print(f"{provider.__name__}:", e)
        
async def run_all():
    calls = [
        run_provider(provider) for provider in _providers
    ]
asyncio.run(run_all())