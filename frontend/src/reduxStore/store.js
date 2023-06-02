import {createStore, applyMiddleware, compose} from 'redux'
import createSagaMiddleware from 'redux-saga'
import {combinedReducers} from './rootReducer'
import {rootSaga} from './rootSaga'
import {createBrowserHistory} from 'history'
import { persistStore } from 'redux-persist'

const sagaMiddleware = createSagaMiddleware()
export const history = createBrowserHistory()

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const middlewares = [sagaMiddleware /** more middlewares if any goes here */];

const store = createStore(combinedReducers, composeEnhancers(applyMiddleware(...middlewares)))
const persistor = persistStore(store)

sagaMiddleware.run(rootSaga)

export {store, persistor}
