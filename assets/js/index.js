var React = require('react')
var ReactDOM = require('react-dom')

var Hello = React.createClass ({
    render: function() {
        return (
            <h1>
            Hello World, Welcome to React!
            </h1>
        )
    }
})

ReactDOM.render(<Hello />, document.getElementById('container'))
