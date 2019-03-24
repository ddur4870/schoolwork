import os
from bottle import route, run, template

index_html =''' <p><strong>Gay pornography</strong> is the representation of <a title="Human sexual activity" href="https://en.wikipedia.org/wiki/Human_sexual_activity">sexual activity</a> between males. Its primary goal is <a title="Sexual arousal" href="https://en.wikipedia.org/wiki/Sexual_arousal">sexual arousal</a> in its audience. <a title="Softcore pornography" href="https://en.wikipedia.org/wiki/Softcore_pornography">Softcore</a> <a title="Gay" href="https://en.wikipedia.org/wiki/Gay">gay</a> <a title="Pornography" href="https://en.wikipedia.org/wiki/Pornography">pornography</a> also exists; it at one time constituted the <a title="Pornography" href="https://en.wikipedia.org/wiki/Pornography">genre</a>, and may be produced as <a title="Beefcake" href="https://en.wikipedia.org/wiki/Beefcake">beefcake</a> pornography for <a title="Heterosexuality" href="https://en.wikipedia.org/wiki/Heterosexuality">heterosexual</a> female and <a title="Homosexuality" href="https://en.wikipedia.org/wiki/Homosexuality">homosexual</a> male consumption.<sup id="cite_ref-1" class="reference"><a href="https://en.wikipedia.org/wiki/Gay_pornography#cite_note-1">[1]</a></sup></p>'''


@route('/')
def index():
    return template(index_html, author='god')


@route('/name/<name>')
def name(name):
    return template(index_html, author=name)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
