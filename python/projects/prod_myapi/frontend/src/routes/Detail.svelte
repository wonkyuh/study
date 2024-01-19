<script>
    import fastapi from '../lib/api'
    export let params = {}
    let question_id = params.question_id

    let question ={}
    function get_quetsion() {
        fastapi("get", "/api/question/detail/"+question_id, {}, (json) => {
            question=json
        })
    }
    get_quetsion()
</script>

<h1>{question.subject}</h1>
<div>
    {question.content}
</div>

