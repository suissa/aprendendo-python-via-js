fs = require('fs')
testFolder = './actions/'

actions = {}

fs.readdirSync(testFolder).forEach(file => {
  console.log(file)
  name = file.split('.js')[0]
  console.log(file, name)

  actions[name] = require(testFolder+file)
})

console.log(actions, actions.add(2, 3) )