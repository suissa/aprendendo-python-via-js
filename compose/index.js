const compose = ( f1, f2 ) => value => f1( f2( value ) )

const add7 = ( x ) => x + 7
const times10 = ( x ) => x * 10

const runCompose = ( x ) => compose( add7, times10 )( x )

console.log( runCompose( 5 ) ) // 57 = 5 * 10 = 50 + 7

