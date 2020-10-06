// Generated from BKIT.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BKITParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		Integer_literal=1, Float_literal=2, String_literal=3, RETURN=4, INT=5, 
		FLOAT=6, PLUS_INT=7, MINUS_INT=8, STAR_INT=9, DIV_INT=10, LEFT_PAREN=11, 
		RIGHT_PAREN=12, LEFT_BRACKET=13, RIGHT_BRACKET=14, LEFT_BRACE=15, RIGHT_BRACE=16, 
		COLON=17, DOT=18, SEMI=19, COMMA=20, ASSIGN=21, ID=22, ILLEGAL_ESCAPE=23, 
		UNCLOSE_STRING=24, COMMENT=25, UNTERMINATED_COMMENT=26, ERROR_CHAR=27, 
		WS=28;
	public static final int
		RULE_program = 0, RULE_var_declare = 1, RULE_function_declare = 2, RULE_function_body = 3, 
		RULE_ids_list_with_type = 4, RULE_stmt = 5, RULE_assign_stmt = 6, RULE_call_stmt = 7, 
		RULE_ret_stmt = 8, RULE_exprs_list = 9, RULE_expr = 10, RULE_expr0 = 11, 
		RULE_expr1 = 12, RULE_expr2 = 13, RULE_subexpr = 14, RULE_operand = 15, 
		RULE_ids_list = 16, RULE_primitive_type = 17;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "var_declare", "function_declare", "function_body", "ids_list_with_type", 
			"stmt", "assign_stmt", "call_stmt", "ret_stmt", "exprs_list", "expr", 
			"expr0", "expr1", "expr2", "subexpr", "operand", "ids_list", "primitive_type"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, "'+'", "'-'", "'*'", "'/'", 
			"'('", "')'", "'['", "']'", "'{'", "'}'", "':'", "'.'", "';'", "','", 
			"'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "Integer_literal", "Float_literal", "String_literal", "RETURN", 
			"INT", "FLOAT", "PLUS_INT", "MINUS_INT", "STAR_INT", "DIV_INT", "LEFT_PAREN", 
			"RIGHT_PAREN", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", 
			"COLON", "DOT", "SEMI", "COMMA", "ASSIGN", "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
			"COMMENT", "UNTERMINATED_COMMENT", "ERROR_CHAR", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "BKIT.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BKITParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(BKITParser.EOF, 0); }
		public List<Var_declareContext> var_declare() {
			return getRuleContexts(Var_declareContext.class);
		}
		public Var_declareContext var_declare(int i) {
			return getRuleContext(Var_declareContext.class,i);
		}
		public List<Function_declareContext> function_declare() {
			return getRuleContexts(Function_declareContext.class);
		}
		public Function_declareContext function_declare(int i) {
			return getRuleContext(Function_declareContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(38);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(36);
					var_declare();
					}
					break;
				case 2:
					{
					setState(37);
					function_declare();
					}
					break;
				}
				}
				setState(40); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==INT || _la==FLOAT );
			setState(42);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_declareContext extends ParserRuleContext {
		public Ids_list_with_typeContext ids_list_with_type() {
			return getRuleContext(Ids_list_with_typeContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public Var_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_declare; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterVar_declare(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitVar_declare(this);
		}
	}

	public final Var_declareContext var_declare() throws RecognitionException {
		Var_declareContext _localctx = new Var_declareContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_var_declare);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			ids_list_with_type();
			setState(45);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_declareContext extends ParserRuleContext {
		public Primitive_typeContext primitive_type() {
			return getRuleContext(Primitive_typeContext.class,0);
		}
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode LEFT_PAREN() { return getToken(BKITParser.LEFT_PAREN, 0); }
		public TerminalNode RIGHT_PAREN() { return getToken(BKITParser.RIGHT_PAREN, 0); }
		public TerminalNode LEFT_BRACE() { return getToken(BKITParser.LEFT_BRACE, 0); }
		public Function_bodyContext function_body() {
			return getRuleContext(Function_bodyContext.class,0);
		}
		public TerminalNode RIGHT_BRACE() { return getToken(BKITParser.RIGHT_BRACE, 0); }
		public List<Ids_list_with_typeContext> ids_list_with_type() {
			return getRuleContexts(Ids_list_with_typeContext.class);
		}
		public Ids_list_with_typeContext ids_list_with_type(int i) {
			return getRuleContext(Ids_list_with_typeContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(BKITParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(BKITParser.SEMI, i);
		}
		public Function_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_declare; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterFunction_declare(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitFunction_declare(this);
		}
	}

	public final Function_declareContext function_declare() throws RecognitionException {
		Function_declareContext _localctx = new Function_declareContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_function_declare);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			primitive_type();
			setState(48);
			match(ID);
			setState(49);
			match(LEFT_PAREN);
			setState(58);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INT || _la==FLOAT) {
				{
				setState(50);
				ids_list_with_type();
				setState(55);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==SEMI) {
					{
					{
					setState(51);
					match(SEMI);
					setState(52);
					ids_list_with_type();
					}
					}
					setState(57);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(60);
			match(RIGHT_PAREN);
			setState(61);
			match(LEFT_BRACE);
			setState(62);
			function_body();
			setState(63);
			match(RIGHT_BRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_bodyContext extends ParserRuleContext {
		public List<Var_declareContext> var_declare() {
			return getRuleContexts(Var_declareContext.class);
		}
		public Var_declareContext var_declare(int i) {
			return getRuleContext(Var_declareContext.class,i);
		}
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public Function_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_body; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterFunction_body(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitFunction_body(this);
		}
	}

	public final Function_bodyContext function_body() throws RecognitionException {
		Function_bodyContext _localctx = new Function_bodyContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_function_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << INT) | (1L << FLOAT) | (1L << ID))) != 0)) {
				{
				setState(67);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case INT:
				case FLOAT:
					{
					setState(65);
					var_declare();
					}
					break;
				case RETURN:
				case ID:
					{
					setState(66);
					stmt();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(71);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Ids_list_with_typeContext extends ParserRuleContext {
		public Primitive_typeContext primitive_type() {
			return getRuleContext(Primitive_typeContext.class,0);
		}
		public Ids_listContext ids_list() {
			return getRuleContext(Ids_listContext.class,0);
		}
		public Ids_list_with_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ids_list_with_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterIds_list_with_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitIds_list_with_type(this);
		}
	}

	public final Ids_list_with_typeContext ids_list_with_type() throws RecognitionException {
		Ids_list_with_typeContext _localctx = new Ids_list_with_typeContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_ids_list_with_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			primitive_type();
			setState(73);
			ids_list();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StmtContext extends ParserRuleContext {
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public Assign_stmtContext assign_stmt() {
			return getRuleContext(Assign_stmtContext.class,0);
		}
		public Call_stmtContext call_stmt() {
			return getRuleContext(Call_stmtContext.class,0);
		}
		public Ret_stmtContext ret_stmt() {
			return getRuleContext(Ret_stmtContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitStmt(this);
		}
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(75);
				assign_stmt();
				}
				break;
			case 2:
				{
				setState(76);
				call_stmt();
				}
				break;
			case 3:
				{
				setState(77);
				ret_stmt();
				}
				break;
			}
			setState(80);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_stmtContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(BKITParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Assign_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterAssign_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitAssign_stmt(this);
		}
	}

	public final Assign_stmtContext assign_stmt() throws RecognitionException {
		Assign_stmtContext _localctx = new Assign_stmtContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_assign_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			match(ID);
			setState(83);
			match(ASSIGN);
			setState(84);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Call_stmtContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode LEFT_PAREN() { return getToken(BKITParser.LEFT_PAREN, 0); }
		public TerminalNode RIGHT_PAREN() { return getToken(BKITParser.RIGHT_PAREN, 0); }
		public List<Exprs_listContext> exprs_list() {
			return getRuleContexts(Exprs_listContext.class);
		}
		public Exprs_listContext exprs_list(int i) {
			return getRuleContext(Exprs_listContext.class,i);
		}
		public Call_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterCall_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitCall_stmt(this);
		}
	}

	public final Call_stmtContext call_stmt() throws RecognitionException {
		Call_stmtContext _localctx = new Call_stmtContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_call_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(ID);
			setState(87);
			match(LEFT_PAREN);
			setState(91);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Integer_literal) | (1L << Float_literal) | (1L << LEFT_PAREN) | (1L << ID))) != 0)) {
				{
				{
				setState(88);
				exprs_list(0);
				}
				}
				setState(93);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(94);
			match(RIGHT_PAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Ret_stmtContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(BKITParser.RETURN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Ret_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ret_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterRet_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitRet_stmt(this);
		}
	}

	public final Ret_stmtContext ret_stmt() throws RecognitionException {
		Ret_stmtContext _localctx = new Ret_stmtContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_ret_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			match(RETURN);
			setState(97);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exprs_listContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Exprs_listContext exprs_list() {
			return getRuleContext(Exprs_listContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(BKITParser.COMMA, 0); }
		public Exprs_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprs_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExprs_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExprs_list(this);
		}
	}

	public final Exprs_listContext exprs_list() throws RecognitionException {
		return exprs_list(0);
	}

	private Exprs_listContext exprs_list(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Exprs_listContext _localctx = new Exprs_listContext(_ctx, _parentState);
		Exprs_listContext _prevctx = _localctx;
		int _startState = 18;
		enterRecursionRule(_localctx, 18, RULE_exprs_list, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(100);
			expr();
			}
			_ctx.stop = _input.LT(-1);
			setState(107);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Exprs_listContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exprs_list);
					setState(102);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(103);
					match(COMMA);
					setState(104);
					expr();
					}
					} 
				}
				setState(109);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public Expr0Context expr0() {
			return getRuleContext(Expr0Context.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			expr0();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr0Context extends ParserRuleContext {
		public Expr1Context expr1() {
			return getRuleContext(Expr1Context.class,0);
		}
		public TerminalNode PLUS_INT() { return getToken(BKITParser.PLUS_INT, 0); }
		public Expr0Context expr0() {
			return getRuleContext(Expr0Context.class,0);
		}
		public Expr0Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr0; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExpr0(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExpr0(this);
		}
	}

	public final Expr0Context expr0() throws RecognitionException {
		Expr0Context _localctx = new Expr0Context(_ctx, getState());
		enterRule(_localctx, 22, RULE_expr0);
		try {
			setState(117);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(112);
				expr1(0);
				setState(113);
				match(PLUS_INT);
				setState(114);
				expr0();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(116);
				expr1(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr1Context extends ParserRuleContext {
		public Expr2Context expr2() {
			return getRuleContext(Expr2Context.class,0);
		}
		public List<Expr1Context> expr1() {
			return getRuleContexts(Expr1Context.class);
		}
		public Expr1Context expr1(int i) {
			return getRuleContext(Expr1Context.class,i);
		}
		public TerminalNode MINUS_INT() { return getToken(BKITParser.MINUS_INT, 0); }
		public Expr1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr1; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExpr1(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExpr1(this);
		}
	}

	public final Expr1Context expr1() throws RecognitionException {
		return expr1(0);
	}

	private Expr1Context expr1(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr1Context _localctx = new Expr1Context(_ctx, _parentState);
		Expr1Context _prevctx = _localctx;
		int _startState = 24;
		enterRecursionRule(_localctx, 24, RULE_expr1, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(120);
			expr2(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(127);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr1Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr1);
					setState(122);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(123);
					match(MINUS_INT);
					setState(124);
					expr1(3);
					}
					} 
				}
				setState(129);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Expr2Context extends ParserRuleContext {
		public OperandContext operand() {
			return getRuleContext(OperandContext.class,0);
		}
		public Expr2Context expr2() {
			return getRuleContext(Expr2Context.class,0);
		}
		public TerminalNode DIV_INT() { return getToken(BKITParser.DIV_INT, 0); }
		public TerminalNode STAR_INT() { return getToken(BKITParser.STAR_INT, 0); }
		public Expr2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr2; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExpr2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExpr2(this);
		}
	}

	public final Expr2Context expr2() throws RecognitionException {
		return expr2(0);
	}

	private Expr2Context expr2(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr2Context _localctx = new Expr2Context(_ctx, _parentState);
		Expr2Context _prevctx = _localctx;
		int _startState = 26;
		enterRecursionRule(_localctx, 26, RULE_expr2, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(131);
			operand();
			}
			_ctx.stop = _input.LT(-1);
			setState(141);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(139);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
					case 1:
						{
						_localctx = new Expr2Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr2);
						setState(133);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(134);
						match(DIV_INT);
						setState(135);
						operand();
						}
						break;
					case 2:
						{
						_localctx = new Expr2Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr2);
						setState(136);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(137);
						match(STAR_INT);
						setState(138);
						operand();
						}
						break;
					}
					} 
				}
				setState(143);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class SubexprContext extends ParserRuleContext {
		public TerminalNode LEFT_PAREN() { return getToken(BKITParser.LEFT_PAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RIGHT_PAREN() { return getToken(BKITParser.RIGHT_PAREN, 0); }
		public SubexprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subexpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterSubexpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitSubexpr(this);
		}
	}

	public final SubexprContext subexpr() throws RecognitionException {
		SubexprContext _localctx = new SubexprContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_subexpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			match(LEFT_PAREN);
			setState(145);
			expr();
			setState(146);
			match(RIGHT_PAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OperandContext extends ParserRuleContext {
		public TerminalNode Integer_literal() { return getToken(BKITParser.Integer_literal, 0); }
		public TerminalNode Float_literal() { return getToken(BKITParser.Float_literal, 0); }
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public Call_stmtContext call_stmt() {
			return getRuleContext(Call_stmtContext.class,0);
		}
		public SubexprContext subexpr() {
			return getRuleContext(SubexprContext.class,0);
		}
		public OperandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operand; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterOperand(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitOperand(this);
		}
	}

	public final OperandContext operand() throws RecognitionException {
		OperandContext _localctx = new OperandContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_operand);
		try {
			setState(153);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(148);
				match(Integer_literal);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(149);
				match(Float_literal);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(150);
				match(ID);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(151);
				call_stmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(152);
				subexpr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Ids_listContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(BKITParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(BKITParser.ID, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public Ids_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ids_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterIds_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitIds_list(this);
		}
	}

	public final Ids_listContext ids_list() throws RecognitionException {
		Ids_listContext _localctx = new Ids_listContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_ids_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			match(ID);
			setState(160);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(156);
				match(COMMA);
				setState(157);
				match(ID);
				}
				}
				setState(162);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Primitive_typeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(BKITParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(BKITParser.FLOAT, 0); }
		public Primitive_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitive_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterPrimitive_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitPrimitive_type(this);
		}
	}

	public final Primitive_typeContext primitive_type() throws RecognitionException {
		Primitive_typeContext _localctx = new Primitive_typeContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_primitive_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==FLOAT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 9:
			return exprs_list_sempred((Exprs_listContext)_localctx, predIndex);
		case 12:
			return expr1_sempred((Expr1Context)_localctx, predIndex);
		case 13:
			return expr2_sempred((Expr2Context)_localctx, predIndex);
		}
		return true;
	}
	private boolean exprs_list_sempred(Exprs_listContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean expr1_sempred(Expr1Context _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr2_sempred(Expr2Context _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 3);
		case 3:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36\u00a8\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\3\2\3\2\6\2)\n\2\r\2\16\2*\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\7\48\n\4\f\4\16\4;\13\4\5\4=\n\4\3\4\3\4\3\4\3\4\3\4\3\5"+
		"\3\5\7\5F\n\5\f\5\16\5I\13\5\3\6\3\6\3\6\3\7\3\7\3\7\5\7Q\n\7\3\7\3\7"+
		"\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7\t\\\n\t\f\t\16\t_\13\t\3\t\3\t\3\n\3\n"+
		"\3\n\3\13\3\13\3\13\3\13\3\13\3\13\7\13l\n\13\f\13\16\13o\13\13\3\f\3"+
		"\f\3\r\3\r\3\r\3\r\3\r\5\rx\n\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u0080"+
		"\n\16\f\16\16\16\u0083\13\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\7\17\u008e\n\17\f\17\16\17\u0091\13\17\3\20\3\20\3\20\3\20\3\21\3"+
		"\21\3\21\3\21\3\21\5\21\u009c\n\21\3\22\3\22\3\22\7\22\u00a1\n\22\f\22"+
		"\16\22\u00a4\13\22\3\23\3\23\3\23\2\5\24\32\34\24\2\4\6\b\n\f\16\20\22"+
		"\24\26\30\32\34\36 \"$\2\3\3\2\7\b\2\u00a8\2(\3\2\2\2\4.\3\2\2\2\6\61"+
		"\3\2\2\2\bG\3\2\2\2\nJ\3\2\2\2\fP\3\2\2\2\16T\3\2\2\2\20X\3\2\2\2\22b"+
		"\3\2\2\2\24e\3\2\2\2\26p\3\2\2\2\30w\3\2\2\2\32y\3\2\2\2\34\u0084\3\2"+
		"\2\2\36\u0092\3\2\2\2 \u009b\3\2\2\2\"\u009d\3\2\2\2$\u00a5\3\2\2\2&)"+
		"\5\4\3\2\')\5\6\4\2(&\3\2\2\2(\'\3\2\2\2)*\3\2\2\2*(\3\2\2\2*+\3\2\2\2"+
		"+,\3\2\2\2,-\7\2\2\3-\3\3\2\2\2./\5\n\6\2/\60\7\25\2\2\60\5\3\2\2\2\61"+
		"\62\5$\23\2\62\63\7\30\2\2\63<\7\r\2\2\649\5\n\6\2\65\66\7\25\2\2\668"+
		"\5\n\6\2\67\65\3\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:=\3\2\2\2;9\3\2"+
		"\2\2<\64\3\2\2\2<=\3\2\2\2=>\3\2\2\2>?\7\16\2\2?@\7\21\2\2@A\5\b\5\2A"+
		"B\7\22\2\2B\7\3\2\2\2CF\5\4\3\2DF\5\f\7\2EC\3\2\2\2ED\3\2\2\2FI\3\2\2"+
		"\2GE\3\2\2\2GH\3\2\2\2H\t\3\2\2\2IG\3\2\2\2JK\5$\23\2KL\5\"\22\2L\13\3"+
		"\2\2\2MQ\5\16\b\2NQ\5\20\t\2OQ\5\22\n\2PM\3\2\2\2PN\3\2\2\2PO\3\2\2\2"+
		"QR\3\2\2\2RS\7\25\2\2S\r\3\2\2\2TU\7\30\2\2UV\7\27\2\2VW\5\26\f\2W\17"+
		"\3\2\2\2XY\7\30\2\2Y]\7\r\2\2Z\\\5\24\13\2[Z\3\2\2\2\\_\3\2\2\2][\3\2"+
		"\2\2]^\3\2\2\2^`\3\2\2\2_]\3\2\2\2`a\7\16\2\2a\21\3\2\2\2bc\7\6\2\2cd"+
		"\5\26\f\2d\23\3\2\2\2ef\b\13\1\2fg\5\26\f\2gm\3\2\2\2hi\f\3\2\2ij\7\26"+
		"\2\2jl\5\26\f\2kh\3\2\2\2lo\3\2\2\2mk\3\2\2\2mn\3\2\2\2n\25\3\2\2\2om"+
		"\3\2\2\2pq\5\30\r\2q\27\3\2\2\2rs\5\32\16\2st\7\t\2\2tu\5\30\r\2ux\3\2"+
		"\2\2vx\5\32\16\2wr\3\2\2\2wv\3\2\2\2x\31\3\2\2\2yz\b\16\1\2z{\5\34\17"+
		"\2{\u0081\3\2\2\2|}\f\4\2\2}~\7\n\2\2~\u0080\5\32\16\5\177|\3\2\2\2\u0080"+
		"\u0083\3\2\2\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\33\3\2\2\2"+
		"\u0083\u0081\3\2\2\2\u0084\u0085\b\17\1\2\u0085\u0086\5 \21\2\u0086\u008f"+
		"\3\2\2\2\u0087\u0088\f\5\2\2\u0088\u0089\7\f\2\2\u0089\u008e\5 \21\2\u008a"+
		"\u008b\f\4\2\2\u008b\u008c\7\13\2\2\u008c\u008e\5 \21\2\u008d\u0087\3"+
		"\2\2\2\u008d\u008a\3\2\2\2\u008e\u0091\3\2\2\2\u008f\u008d\3\2\2\2\u008f"+
		"\u0090\3\2\2\2\u0090\35\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093\7\r\2"+
		"\2\u0093\u0094\5\26\f\2\u0094\u0095\7\16\2\2\u0095\37\3\2\2\2\u0096\u009c"+
		"\7\3\2\2\u0097\u009c\7\4\2\2\u0098\u009c\7\30\2\2\u0099\u009c\5\20\t\2"+
		"\u009a\u009c\5\36\20\2\u009b\u0096\3\2\2\2\u009b\u0097\3\2\2\2\u009b\u0098"+
		"\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009a\3\2\2\2\u009c!\3\2\2\2\u009d"+
		"\u00a2\7\30\2\2\u009e\u009f\7\26\2\2\u009f\u00a1\7\30\2\2\u00a0\u009e"+
		"\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3"+
		"#\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a6\t\2\2\2\u00a6%\3\2\2\2\21(*"+
		"9<EGP]mw\u0081\u008d\u008f\u009b\u00a2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}