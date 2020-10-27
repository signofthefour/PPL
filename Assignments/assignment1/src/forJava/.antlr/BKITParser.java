// Generated from /home/nguyendat/Documents/projects/PPL/Assignments/assignment1/src/forJava/BKIT.g4 by ANTLR 4.8
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
		ID=1, INT_LIT=2, FLOAT_LIT=3, BOOL_LIT=4, STRING_LIT=5, BODY=6, BREAK=7, 
		CONTINUE=8, DO=9, ELSE=10, ELSEIF=11, ENDIF=12, ENDBODY=13, ENDFOR=14, 
		ENDWHILE=15, FOR=16, FUNCTION=17, IF=18, PARAMETER=19, RETURN=20, THEN=21, 
		VAR=22, WHILE=23, TRUE=24, FALSE=25, ENDDO=26, PLUS_INT=27, PLUS_FLOAT=28, 
		MINUS_INT=29, MINUS_FLOAT=30, STAR_INT=31, STAR_FLOAT=32, DIV_INT=33, 
		DIV_FLOAT=34, MOD=35, NOT=36, AND=37, OR=38, EQUAL=39, NOT_EQUAL_INT=40, 
		LESS_INT=41, GREATER_INT=42, LESS_OR_EQUAL_INT=43, GREATER_OR_EQUAL_INT=44, 
		NOT_EQUAL_FLOAT=45, LESS_FLOAT=46, GREATER_FLOAT=47, LESS_OR_EQUAL_FLOAT=48, 
		GREATER_OR_EQUAL_FLOAT=49, LEFT_PAREN=50, RIGHT_PAREN=51, LEFT_BRACKET=52, 
		RIGHT_BRACKET=53, LEFT_BRACE=54, RIGHT_BRACE=55, COLON=56, DOT=57, SEMI=58, 
		COMMA=59, ASSIGN=60, DOUBLE_QUOTE=61, INT_OF_FLOAT=62, INT_OF_STRING=63, 
		FLOAT_TO_INT=64, FLOAT_OF_STRING=65, BOOL_OF_STRING=66, STRING_OF_BOOL=67, 
		STRING_OF_INT=68, STRING_OF_FLOAT=69, COMMENT=70, WS=71, ILLEGAL_ESCAPE=72, 
		UNCLOSE_STRING=73, UNTERMINATED_COMMENT=74, ERROR_CHAR=75;
	public static final int
		RULE_program = 0, RULE_var_declare = 1, RULE_function_declare = 2, RULE_array = 3, 
		RULE_primitive_data = 4, RULE_composite_data = 5, RULE_array_lit = 6, 
		RULE_var_list = 7, RULE_scalar_var = 8, RULE_var_non_init = 9, RULE_composite_var = 10, 
		RULE_var_init = 11, RULE_composite_init = 12, RULE_primitive_init = 13, 
		RULE_params_list = 14, RULE_stmt_list = 15, RULE_stmt = 16, RULE_if_stmt = 17, 
		RULE_var_declare_stmt = 18, RULE_for_stmt = 19, RULE_while_stmt = 20, 
		RULE_dowhile_stmt = 21, RULE_assign_stmt = 22, RULE_break_stmt = 23, RULE_continue_stmt = 24, 
		RULE_call_stmt = 25, RULE_return_stmt = 26, RULE_init_for = 27, RULE_con_for = 28, 
		RULE_update_for = 29, RULE_expr = 30, RULE_expr1 = 31, RULE_expr2 = 32, 
		RULE_expr3 = 33, RULE_expr4 = 34, RULE_expr5 = 35, RULE_expr6 = 36, RULE_expr7 = 37, 
		RULE_expr8 = 38, RULE_operand = 39, RULE_function_call = 40, RULE_index_op = 41;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "var_declare", "function_declare", "array", "primitive_data", 
			"composite_data", "array_lit", "var_list", "scalar_var", "var_non_init", 
			"composite_var", "var_init", "composite_init", "primitive_init", "params_list", 
			"stmt_list", "stmt", "if_stmt", "var_declare_stmt", "for_stmt", "while_stmt", 
			"dowhile_stmt", "assign_stmt", "break_stmt", "continue_stmt", "call_stmt", 
			"return_stmt", "init_for", "con_for", "update_for", "expr", "expr1", 
			"expr2", "expr3", "expr4", "expr5", "expr6", "expr7", "expr8", "operand", 
			"function_call", "index_op"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, "'Body'", "'Break'", "'Continue'", 
			"'Do'", "'Else'", "'ElseIf'", "'EndIf'", "'EndBody'", "'EndFor'", "'EndWhile'", 
			"'For'", "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", 
			"'While'", "'True'", "'False'", "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", 
			"'*'", "'*.'", "'\\'", "'\\.'", "'\\%'", "'!'", "'&&'", "'||'", "'=='", 
			"'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", 
			"'>=.'", "'('", "')'", "'['", "']'", "'{'", "'}'", "':'", "'.'", "';'", 
			"','", "'='", "'\"'", "'int_of_float'", "'int_of_string'", "'float_to_int'", 
			"'float_of_string'", "'bool_of_string'", "'string_of_bool'", "'string_of_int'", 
			"'string_of_float'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ID", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", "BODY", 
			"BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDIF", "ENDBODY", "ENDFOR", 
			"ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "VAR", 
			"WHILE", "TRUE", "FALSE", "ENDDO", "PLUS_INT", "PLUS_FLOAT", "MINUS_INT", 
			"MINUS_FLOAT", "STAR_INT", "STAR_FLOAT", "DIV_INT", "DIV_FLOAT", "MOD", 
			"NOT", "AND", "OR", "EQUAL", "NOT_EQUAL_INT", "LESS_INT", "GREATER_INT", 
			"LESS_OR_EQUAL_INT", "GREATER_OR_EQUAL_INT", "NOT_EQUAL_FLOAT", "LESS_FLOAT", 
			"GREATER_FLOAT", "LESS_OR_EQUAL_FLOAT", "GREATER_OR_EQUAL_FLOAT", "LEFT_PAREN", 
			"RIGHT_PAREN", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", 
			"COLON", "DOT", "SEMI", "COMMA", "ASSIGN", "DOUBLE_QUOTE", "INT_OF_FLOAT", 
			"INT_OF_STRING", "FLOAT_TO_INT", "FLOAT_OF_STRING", "BOOL_OF_STRING", 
			"STRING_OF_BOOL", "STRING_OF_INT", "STRING_OF_FLOAT", "COMMENT", "WS", 
			"ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", "ERROR_CHAR"
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
		public List<TerminalNode> SEMI() { return getTokens(BKITParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(BKITParser.SEMI, i);
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
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(84);
				var_declare();
				setState(85);
				match(SEMI);
				}
				}
				setState(91);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(95);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION) {
				{
				{
				setState(92);
				function_declare();
				}
				}
				setState(97);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(98);
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
		public TerminalNode VAR() { return getToken(BKITParser.VAR, 0); }
		public TerminalNode COLON() { return getToken(BKITParser.COLON, 0); }
		public Var_listContext var_list() {
			return getRuleContext(Var_listContext.class,0);
		}
		public Var_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_declare; }
	}

	public final Var_declareContext var_declare() throws RecognitionException {
		Var_declareContext _localctx = new Var_declareContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_var_declare);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			match(VAR);
			setState(101);
			match(COLON);
			setState(102);
			var_list();
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
		public TerminalNode FUNCTION() { return getToken(BKITParser.FUNCTION, 0); }
		public List<TerminalNode> COLON() { return getTokens(BKITParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(BKITParser.COLON, i);
		}
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode BODY() { return getToken(BKITParser.BODY, 0); }
		public TerminalNode ENDBODY() { return getToken(BKITParser.ENDBODY, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public TerminalNode PARAMETER() { return getToken(BKITParser.PARAMETER, 0); }
		public Params_listContext params_list() {
			return getRuleContext(Params_listContext.class,0);
		}
		public List<Var_declare_stmtContext> var_declare_stmt() {
			return getRuleContexts(Var_declare_stmtContext.class);
		}
		public Var_declare_stmtContext var_declare_stmt(int i) {
			return getRuleContext(Var_declare_stmtContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(BKITParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(BKITParser.SEMI, i);
		}
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public Function_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_declare; }
	}

	public final Function_declareContext function_declare() throws RecognitionException {
		Function_declareContext _localctx = new Function_declareContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_function_declare);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			match(FUNCTION);
			setState(105);
			match(COLON);
			setState(106);
			match(ID);
			setState(110);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PARAMETER) {
				{
				setState(107);
				match(PARAMETER);
				setState(108);
				match(COLON);
				setState(109);
				params_list();
				}
			}

			setState(112);
			match(BODY);
			setState(113);
			match(COLON);
			setState(119);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(114);
				var_declare_stmt();
				setState(115);
				match(SEMI);
				}
				}
				setState(121);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(125);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ID) | (1L << BREAK) | (1L << CONTINUE) | (1L << DO) | (1L << FOR) | (1L << IF) | (1L << RETURN) | (1L << WHILE))) != 0)) {
				{
				{
				setState(122);
				stmt();
				}
				}
				setState(127);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(128);
			match(ENDBODY);
			setState(129);
			match(DOT);
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

	public static class ArrayContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(BKITParser.ASSIGN, 0); }
		public Array_litContext array_lit() {
			return getRuleContext(Array_litContext.class,0);
		}
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_array);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			match(ID);
			setState(132);
			match(ASSIGN);
			setState(133);
			array_lit();
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

	public static class Primitive_dataContext extends ParserRuleContext {
		public TerminalNode INT_LIT() { return getToken(BKITParser.INT_LIT, 0); }
		public TerminalNode FLOAT_LIT() { return getToken(BKITParser.FLOAT_LIT, 0); }
		public TerminalNode STRING_LIT() { return getToken(BKITParser.STRING_LIT, 0); }
		public TerminalNode BOOL_LIT() { return getToken(BKITParser.BOOL_LIT, 0); }
		public Primitive_dataContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitive_data; }
	}

	public final Primitive_dataContext primitive_data() throws RecognitionException {
		Primitive_dataContext _localctx = new Primitive_dataContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_primitive_data);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT_LIT) | (1L << FLOAT_LIT) | (1L << BOOL_LIT) | (1L << STRING_LIT))) != 0)) ) {
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

	public static class Composite_dataContext extends ParserRuleContext {
		public Array_litContext array_lit() {
			return getRuleContext(Array_litContext.class,0);
		}
		public Composite_dataContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_composite_data; }
	}

	public final Composite_dataContext composite_data() throws RecognitionException {
		Composite_dataContext _localctx = new Composite_dataContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_composite_data);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			array_lit();
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

	public static class Array_litContext extends ParserRuleContext {
		public TerminalNode LEFT_BRACE() { return getToken(BKITParser.LEFT_BRACE, 0); }
		public TerminalNode RIGHT_BRACE() { return getToken(BKITParser.RIGHT_BRACE, 0); }
		public List<Primitive_dataContext> primitive_data() {
			return getRuleContexts(Primitive_dataContext.class);
		}
		public Primitive_dataContext primitive_data(int i) {
			return getRuleContext(Primitive_dataContext.class,i);
		}
		public List<Composite_dataContext> composite_data() {
			return getRuleContexts(Composite_dataContext.class);
		}
		public Composite_dataContext composite_data(int i) {
			return getRuleContext(Composite_dataContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public Array_litContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_lit; }
	}

	public final Array_litContext array_lit() throws RecognitionException {
		Array_litContext _localctx = new Array_litContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_array_lit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			match(LEFT_BRACE);
			setState(142);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_LIT:
			case FLOAT_LIT:
			case BOOL_LIT:
			case STRING_LIT:
				{
				setState(140);
				primitive_data();
				}
				break;
			case LEFT_BRACE:
				{
				setState(141);
				composite_data();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(151);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(144);
				match(COMMA);
				setState(147);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case INT_LIT:
				case FLOAT_LIT:
				case BOOL_LIT:
				case STRING_LIT:
					{
					setState(145);
					primitive_data();
					}
					break;
				case LEFT_BRACE:
					{
					setState(146);
					composite_data();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				}
				setState(153);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(154);
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

	public static class Var_listContext extends ParserRuleContext {
		public List<Var_non_initContext> var_non_init() {
			return getRuleContexts(Var_non_initContext.class);
		}
		public Var_non_initContext var_non_init(int i) {
			return getRuleContext(Var_non_initContext.class,i);
		}
		public List<Var_initContext> var_init() {
			return getRuleContexts(Var_initContext.class);
		}
		public Var_initContext var_init(int i) {
			return getRuleContext(Var_initContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public Var_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_list; }
	}

	public final Var_listContext var_list() throws RecognitionException {
		Var_listContext _localctx = new Var_listContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_var_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				setState(156);
				var_non_init();
				}
				break;
			case 2:
				{
				setState(157);
				var_init();
				}
				break;
			}
			setState(167);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(160);
				match(COMMA);
				setState(163);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
				case 1:
					{
					setState(161);
					var_non_init();
					}
					break;
				case 2:
					{
					setState(162);
					var_init();
					}
					break;
				}
				}
				}
				setState(169);
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

	public static class Scalar_varContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public Scalar_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scalar_var; }
	}

	public final Scalar_varContext scalar_var() throws RecognitionException {
		Scalar_varContext _localctx = new Scalar_varContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_scalar_var);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
			match(ID);
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

	public static class Var_non_initContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public List<TerminalNode> LEFT_BRACKET() { return getTokens(BKITParser.LEFT_BRACKET); }
		public TerminalNode LEFT_BRACKET(int i) {
			return getToken(BKITParser.LEFT_BRACKET, i);
		}
		public List<TerminalNode> INT_LIT() { return getTokens(BKITParser.INT_LIT); }
		public TerminalNode INT_LIT(int i) {
			return getToken(BKITParser.INT_LIT, i);
		}
		public List<TerminalNode> RIGHT_BRACKET() { return getTokens(BKITParser.RIGHT_BRACKET); }
		public TerminalNode RIGHT_BRACKET(int i) {
			return getToken(BKITParser.RIGHT_BRACKET, i);
		}
		public Var_non_initContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_non_init; }
	}

	public final Var_non_initContext var_non_init() throws RecognitionException {
		Var_non_initContext _localctx = new Var_non_initContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_var_non_init);
		try {
			int _alt;
			setState(181);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(172);
				match(ID);
				setState(176); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(173);
						match(LEFT_BRACKET);
						setState(174);
						match(INT_LIT);
						setState(175);
						match(RIGHT_BRACKET);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(178); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(180);
				match(ID);
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

	public static class Composite_varContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public List<TerminalNode> LEFT_BRACKET() { return getTokens(BKITParser.LEFT_BRACKET); }
		public TerminalNode LEFT_BRACKET(int i) {
			return getToken(BKITParser.LEFT_BRACKET, i);
		}
		public List<TerminalNode> RIGHT_BRACKET() { return getTokens(BKITParser.RIGHT_BRACKET); }
		public TerminalNode RIGHT_BRACKET(int i) {
			return getToken(BKITParser.RIGHT_BRACKET, i);
		}
		public List<Composite_varContext> composite_var() {
			return getRuleContexts(Composite_varContext.class);
		}
		public Composite_varContext composite_var(int i) {
			return getRuleContext(Composite_varContext.class,i);
		}
		public List<TerminalNode> INT_LIT() { return getTokens(BKITParser.INT_LIT); }
		public TerminalNode INT_LIT(int i) {
			return getToken(BKITParser.INT_LIT, i);
		}
		public Composite_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_composite_var; }
	}

	public final Composite_varContext composite_var() throws RecognitionException {
		Composite_varContext _localctx = new Composite_varContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_composite_var);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(183);
			match(ID);
			setState(190); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(184);
				match(LEFT_BRACKET);
				setState(187);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ID:
					{
					setState(185);
					composite_var();
					}
					break;
				case INT_LIT:
					{
					setState(186);
					match(INT_LIT);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(189);
				match(RIGHT_BRACKET);
				}
				}
				setState(192); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LEFT_BRACKET );
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

	public static class Var_initContext extends ParserRuleContext {
		public TerminalNode ASSIGN() { return getToken(BKITParser.ASSIGN, 0); }
		public Composite_varContext composite_var() {
			return getRuleContext(Composite_varContext.class,0);
		}
		public Scalar_varContext scalar_var() {
			return getRuleContext(Scalar_varContext.class,0);
		}
		public Composite_dataContext composite_data() {
			return getRuleContext(Composite_dataContext.class,0);
		}
		public Primitive_dataContext primitive_data() {
			return getRuleContext(Primitive_dataContext.class,0);
		}
		public Var_initContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_init; }
	}

	public final Var_initContext var_init() throws RecognitionException {
		Var_initContext _localctx = new Var_initContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_var_init);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(194);
				composite_var();
				}
				break;
			case 2:
				{
				setState(195);
				scalar_var();
				}
				break;
			}
			setState(198);
			match(ASSIGN);
			setState(201);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEFT_BRACE:
				{
				setState(199);
				composite_data();
				}
				break;
			case INT_LIT:
			case FLOAT_LIT:
			case BOOL_LIT:
			case STRING_LIT:
				{
				setState(200);
				primitive_data();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class Composite_initContext extends ParserRuleContext {
		public Composite_varContext composite_var() {
			return getRuleContext(Composite_varContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(BKITParser.ASSIGN, 0); }
		public Array_litContext array_lit() {
			return getRuleContext(Array_litContext.class,0);
		}
		public Composite_initContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_composite_init; }
	}

	public final Composite_initContext composite_init() throws RecognitionException {
		Composite_initContext _localctx = new Composite_initContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_composite_init);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(203);
			composite_var();
			setState(204);
			match(ASSIGN);
			setState(205);
			array_lit();
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

	public static class Primitive_initContext extends ParserRuleContext {
		public Scalar_varContext scalar_var() {
			return getRuleContext(Scalar_varContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(BKITParser.ASSIGN, 0); }
		public Primitive_dataContext primitive_data() {
			return getRuleContext(Primitive_dataContext.class,0);
		}
		public Primitive_initContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitive_init; }
	}

	public final Primitive_initContext primitive_init() throws RecognitionException {
		Primitive_initContext _localctx = new Primitive_initContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_primitive_init);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(207);
			scalar_var();
			setState(208);
			match(ASSIGN);
			setState(209);
			primitive_data();
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

	public static class Params_listContext extends ParserRuleContext {
		public List<Var_non_initContext> var_non_init() {
			return getRuleContexts(Var_non_initContext.class);
		}
		public Var_non_initContext var_non_init(int i) {
			return getRuleContext(Var_non_initContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public Params_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params_list; }
	}

	public final Params_listContext params_list() throws RecognitionException {
		Params_listContext _localctx = new Params_listContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_params_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
			var_non_init();
			setState(216);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(212);
				match(COMMA);
				setState(213);
				var_non_init();
				}
				}
				setState(218);
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

	public static class Stmt_listContext extends ParserRuleContext {
		public List<Var_declare_stmtContext> var_declare_stmt() {
			return getRuleContexts(Var_declare_stmtContext.class);
		}
		public Var_declare_stmtContext var_declare_stmt(int i) {
			return getRuleContext(Var_declare_stmtContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(BKITParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(BKITParser.SEMI, i);
		}
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public Stmt_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt_list; }
	}

	public final Stmt_listContext stmt_list() throws RecognitionException {
		Stmt_listContext _localctx = new Stmt_listContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_stmt_list);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(224);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(219);
				var_declare_stmt();
				setState(220);
				match(SEMI);
				}
				}
				setState(226);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(230);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(227);
					stmt();
					}
					} 
				}
				setState(232);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
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

	public static class StmtContext extends ParserRuleContext {
		public If_stmtContext if_stmt() {
			return getRuleContext(If_stmtContext.class,0);
		}
		public For_stmtContext for_stmt() {
			return getRuleContext(For_stmtContext.class,0);
		}
		public While_stmtContext while_stmt() {
			return getRuleContext(While_stmtContext.class,0);
		}
		public Dowhile_stmtContext dowhile_stmt() {
			return getRuleContext(Dowhile_stmtContext.class,0);
		}
		public Assign_stmtContext assign_stmt() {
			return getRuleContext(Assign_stmtContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public Break_stmtContext break_stmt() {
			return getRuleContext(Break_stmtContext.class,0);
		}
		public Continue_stmtContext continue_stmt() {
			return getRuleContext(Continue_stmtContext.class,0);
		}
		public Call_stmtContext call_stmt() {
			return getRuleContext(Call_stmtContext.class,0);
		}
		public Return_stmtContext return_stmt() {
			return getRuleContext(Return_stmtContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_stmt);
		try {
			setState(252);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(233);
				if_stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(234);
				for_stmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(235);
				while_stmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(236);
				dowhile_stmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(237);
				assign_stmt();
				setState(238);
				match(SEMI);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(240);
				break_stmt();
				setState(241);
				match(SEMI);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(243);
				continue_stmt();
				setState(244);
				match(SEMI);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(246);
				call_stmt();
				setState(247);
				match(SEMI);
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(249);
				return_stmt();
				setState(250);
				match(SEMI);
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

	public static class If_stmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(BKITParser.IF, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> THEN() { return getTokens(BKITParser.THEN); }
		public TerminalNode THEN(int i) {
			return getToken(BKITParser.THEN, i);
		}
		public List<Stmt_listContext> stmt_list() {
			return getRuleContexts(Stmt_listContext.class);
		}
		public Stmt_listContext stmt_list(int i) {
			return getRuleContext(Stmt_listContext.class,i);
		}
		public TerminalNode ENDIF() { return getToken(BKITParser.ENDIF, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public List<TerminalNode> ELSEIF() { return getTokens(BKITParser.ELSEIF); }
		public TerminalNode ELSEIF(int i) {
			return getToken(BKITParser.ELSEIF, i);
		}
		public TerminalNode ELSE() { return getToken(BKITParser.ELSE, 0); }
		public If_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_stmt; }
	}

	public final If_stmtContext if_stmt() throws RecognitionException {
		If_stmtContext _localctx = new If_stmtContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_if_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(254);
			match(IF);
			setState(255);
			expr();
			setState(256);
			match(THEN);
			setState(257);
			stmt_list();
			setState(265);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELSEIF) {
				{
				{
				setState(258);
				match(ELSEIF);
				setState(259);
				expr();
				setState(260);
				match(THEN);
				setState(261);
				stmt_list();
				}
				}
				setState(267);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(270);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(268);
				match(ELSE);
				setState(269);
				stmt_list();
				}
			}

			setState(272);
			match(ENDIF);
			setState(273);
			match(DOT);
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

	public static class Var_declare_stmtContext extends ParserRuleContext {
		public Var_declareContext var_declare() {
			return getRuleContext(Var_declareContext.class,0);
		}
		public Var_declare_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_declare_stmt; }
	}

	public final Var_declare_stmtContext var_declare_stmt() throws RecognitionException {
		Var_declare_stmtContext _localctx = new Var_declare_stmtContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_var_declare_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(275);
			var_declare();
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

	public static class For_stmtContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(BKITParser.FOR, 0); }
		public TerminalNode LEFT_PAREN() { return getToken(BKITParser.LEFT_PAREN, 0); }
		public Init_forContext init_for() {
			return getRuleContext(Init_forContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public Con_forContext con_for() {
			return getRuleContext(Con_forContext.class,0);
		}
		public Update_forContext update_for() {
			return getRuleContext(Update_forContext.class,0);
		}
		public TerminalNode RIGHT_PAREN() { return getToken(BKITParser.RIGHT_PAREN, 0); }
		public TerminalNode DO() { return getToken(BKITParser.DO, 0); }
		public Stmt_listContext stmt_list() {
			return getRuleContext(Stmt_listContext.class,0);
		}
		public TerminalNode ENDFOR() { return getToken(BKITParser.ENDFOR, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public For_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_stmt; }
	}

	public final For_stmtContext for_stmt() throws RecognitionException {
		For_stmtContext _localctx = new For_stmtContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_for_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(277);
			match(FOR);
			setState(278);
			match(LEFT_PAREN);
			setState(279);
			init_for();
			setState(280);
			match(COMMA);
			setState(281);
			con_for();
			setState(282);
			match(COMMA);
			setState(283);
			update_for();
			setState(284);
			match(RIGHT_PAREN);
			setState(285);
			match(DO);
			setState(286);
			stmt_list();
			setState(287);
			match(ENDFOR);
			setState(288);
			match(DOT);
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

	public static class While_stmtContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(BKITParser.WHILE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode DO() { return getToken(BKITParser.DO, 0); }
		public Stmt_listContext stmt_list() {
			return getRuleContext(Stmt_listContext.class,0);
		}
		public TerminalNode ENDWHILE() { return getToken(BKITParser.ENDWHILE, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public While_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_stmt; }
	}

	public final While_stmtContext while_stmt() throws RecognitionException {
		While_stmtContext _localctx = new While_stmtContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(290);
			match(WHILE);
			setState(291);
			expr();
			setState(292);
			match(DO);
			setState(293);
			stmt_list();
			setState(294);
			match(ENDWHILE);
			setState(295);
			match(DOT);
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

	public static class Dowhile_stmtContext extends ParserRuleContext {
		public TerminalNode DO() { return getToken(BKITParser.DO, 0); }
		public Stmt_listContext stmt_list() {
			return getRuleContext(Stmt_listContext.class,0);
		}
		public TerminalNode WHILE() { return getToken(BKITParser.WHILE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode ENDDO() { return getToken(BKITParser.ENDDO, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public Dowhile_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dowhile_stmt; }
	}

	public final Dowhile_stmtContext dowhile_stmt() throws RecognitionException {
		Dowhile_stmtContext _localctx = new Dowhile_stmtContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_dowhile_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(297);
			match(DO);
			setState(298);
			stmt_list();
			setState(299);
			match(WHILE);
			setState(300);
			expr();
			setState(301);
			match(ENDDO);
			setState(302);
			match(DOT);
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
		public Var_non_initContext var_non_init() {
			return getRuleContext(Var_non_initContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(BKITParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Assign_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_stmt; }
	}

	public final Assign_stmtContext assign_stmt() throws RecognitionException {
		Assign_stmtContext _localctx = new Assign_stmtContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_assign_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(304);
			var_non_init();
			setState(305);
			match(ASSIGN);
			{
			setState(306);
			expr();
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

	public static class Break_stmtContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(BKITParser.BREAK, 0); }
		public Break_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_break_stmt; }
	}

	public final Break_stmtContext break_stmt() throws RecognitionException {
		Break_stmtContext _localctx = new Break_stmtContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_break_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(308);
			match(BREAK);
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

	public static class Continue_stmtContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(BKITParser.CONTINUE, 0); }
		public Continue_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continue_stmt; }
	}

	public final Continue_stmtContext continue_stmt() throws RecognitionException {
		Continue_stmtContext _localctx = new Continue_stmtContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_continue_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(310);
			match(CONTINUE);
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
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public Call_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call_stmt; }
	}

	public final Call_stmtContext call_stmt() throws RecognitionException {
		Call_stmtContext _localctx = new Call_stmtContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_call_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(312);
			function_call();
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

	public static class Return_stmtContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(BKITParser.RETURN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Return_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_stmt; }
	}

	public final Return_stmtContext return_stmt() throws RecognitionException {
		Return_stmtContext _localctx = new Return_stmtContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_return_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(314);
			match(RETURN);
			setState(316);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ID) | (1L << INT_LIT) | (1L << FLOAT_LIT) | (1L << BOOL_LIT) | (1L << STRING_LIT) | (1L << MINUS_INT) | (1L << MINUS_FLOAT) | (1L << NOT) | (1L << LEFT_PAREN) | (1L << LEFT_BRACE))) != 0)) {
				{
				setState(315);
				expr();
				}
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

	public static class Init_forContext extends ParserRuleContext {
		public Scalar_varContext scalar_var() {
			return getRuleContext(Scalar_varContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(BKITParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Init_forContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_init_for; }
	}

	public final Init_forContext init_for() throws RecognitionException {
		Init_forContext _localctx = new Init_forContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_init_for);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(318);
			scalar_var();
			setState(319);
			match(ASSIGN);
			setState(320);
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

	public static class Con_forContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Con_forContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_con_for; }
	}

	public final Con_forContext con_for() throws RecognitionException {
		Con_forContext _localctx = new Con_forContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_con_for);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(322);
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

	public static class Update_forContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Update_forContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_update_for; }
	}

	public final Update_forContext update_for() throws RecognitionException {
		Update_forContext _localctx = new Update_forContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_update_for);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(324);
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

	public static class ExprContext extends ParserRuleContext {
		public List<Expr1Context> expr1() {
			return getRuleContexts(Expr1Context.class);
		}
		public Expr1Context expr1(int i) {
			return getRuleContext(Expr1Context.class,i);
		}
		public TerminalNode EQUAL() { return getToken(BKITParser.EQUAL, 0); }
		public TerminalNode NOT_EQUAL_INT() { return getToken(BKITParser.NOT_EQUAL_INT, 0); }
		public TerminalNode LESS_INT() { return getToken(BKITParser.LESS_INT, 0); }
		public TerminalNode GREATER_INT() { return getToken(BKITParser.GREATER_INT, 0); }
		public TerminalNode LESS_OR_EQUAL_INT() { return getToken(BKITParser.LESS_OR_EQUAL_INT, 0); }
		public TerminalNode GREATER_OR_EQUAL_INT() { return getToken(BKITParser.GREATER_OR_EQUAL_INT, 0); }
		public TerminalNode NOT_EQUAL_FLOAT() { return getToken(BKITParser.NOT_EQUAL_FLOAT, 0); }
		public TerminalNode LESS_FLOAT() { return getToken(BKITParser.LESS_FLOAT, 0); }
		public TerminalNode GREATER_FLOAT() { return getToken(BKITParser.GREATER_FLOAT, 0); }
		public TerminalNode LESS_OR_EQUAL_FLOAT() { return getToken(BKITParser.LESS_OR_EQUAL_FLOAT, 0); }
		public TerminalNode GREATER_OR_EQUAL_FLOAT() { return getToken(BKITParser.GREATER_OR_EQUAL_FLOAT, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_expr);
		int _la;
		try {
			setState(331);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(326);
				expr1(0);
				setState(327);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUAL) | (1L << NOT_EQUAL_INT) | (1L << LESS_INT) | (1L << GREATER_INT) | (1L << LESS_OR_EQUAL_INT) | (1L << GREATER_OR_EQUAL_INT) | (1L << NOT_EQUAL_FLOAT) | (1L << LESS_FLOAT) | (1L << GREATER_FLOAT) | (1L << LESS_OR_EQUAL_FLOAT) | (1L << GREATER_OR_EQUAL_FLOAT))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(328);
				expr1(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(330);
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
		public Expr1Context expr1() {
			return getRuleContext(Expr1Context.class,0);
		}
		public TerminalNode AND() { return getToken(BKITParser.AND, 0); }
		public TerminalNode OR() { return getToken(BKITParser.OR, 0); }
		public Expr1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr1; }
	}

	public final Expr1Context expr1() throws RecognitionException {
		return expr1(0);
	}

	private Expr1Context expr1(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr1Context _localctx = new Expr1Context(_ctx, _parentState);
		Expr1Context _prevctx = _localctx;
		int _startState = 62;
		enterRecursionRule(_localctx, 62, RULE_expr1, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(334);
			expr2(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(341);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr1Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr1);
					setState(336);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(337);
					_la = _input.LA(1);
					if ( !(_la==AND || _la==OR) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(338);
					expr2(0);
					}
					} 
				}
				setState(343);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
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
		public Expr3Context expr3() {
			return getRuleContext(Expr3Context.class,0);
		}
		public Expr2Context expr2() {
			return getRuleContext(Expr2Context.class,0);
		}
		public TerminalNode PLUS_FLOAT() { return getToken(BKITParser.PLUS_FLOAT, 0); }
		public TerminalNode PLUS_INT() { return getToken(BKITParser.PLUS_INT, 0); }
		public TerminalNode MINUS_FLOAT() { return getToken(BKITParser.MINUS_FLOAT, 0); }
		public TerminalNode MINUS_INT() { return getToken(BKITParser.MINUS_INT, 0); }
		public Expr2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr2; }
	}

	public final Expr2Context expr2() throws RecognitionException {
		return expr2(0);
	}

	private Expr2Context expr2(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr2Context _localctx = new Expr2Context(_ctx, _parentState);
		Expr2Context _prevctx = _localctx;
		int _startState = 64;
		enterRecursionRule(_localctx, 64, RULE_expr2, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(345);
			expr3(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(352);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr2Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr2);
					setState(347);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(348);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PLUS_INT) | (1L << PLUS_FLOAT) | (1L << MINUS_INT) | (1L << MINUS_FLOAT))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(349);
					expr3(0);
					}
					} 
				}
				setState(354);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
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

	public static class Expr3Context extends ParserRuleContext {
		public Expr4Context expr4() {
			return getRuleContext(Expr4Context.class,0);
		}
		public Expr3Context expr3() {
			return getRuleContext(Expr3Context.class,0);
		}
		public TerminalNode STAR_INT() { return getToken(BKITParser.STAR_INT, 0); }
		public TerminalNode DIV_FLOAT() { return getToken(BKITParser.DIV_FLOAT, 0); }
		public TerminalNode DIV_INT() { return getToken(BKITParser.DIV_INT, 0); }
		public TerminalNode MOD() { return getToken(BKITParser.MOD, 0); }
		public Expr3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr3; }
	}

	public final Expr3Context expr3() throws RecognitionException {
		return expr3(0);
	}

	private Expr3Context expr3(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr3Context _localctx = new Expr3Context(_ctx, _parentState);
		Expr3Context _prevctx = _localctx;
		int _startState = 66;
		enterRecursionRule(_localctx, 66, RULE_expr3, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(356);
			expr4();
			}
			_ctx.stop = _input.LT(-1);
			setState(363);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,27,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr3Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr3);
					setState(358);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(359);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << STAR_INT) | (1L << DIV_INT) | (1L << DIV_FLOAT) | (1L << MOD))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(360);
					expr4();
					}
					} 
				}
				setState(365);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,27,_ctx);
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

	public static class Expr4Context extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(BKITParser.NOT, 0); }
		public Expr4Context expr4() {
			return getRuleContext(Expr4Context.class,0);
		}
		public Expr5Context expr5() {
			return getRuleContext(Expr5Context.class,0);
		}
		public Expr4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr4; }
	}

	public final Expr4Context expr4() throws RecognitionException {
		Expr4Context _localctx = new Expr4Context(_ctx, getState());
		enterRule(_localctx, 68, RULE_expr4);
		try {
			setState(369);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(366);
				match(NOT);
				setState(367);
				expr4();
				}
				break;
			case ID:
			case INT_LIT:
			case FLOAT_LIT:
			case BOOL_LIT:
			case STRING_LIT:
			case MINUS_INT:
			case MINUS_FLOAT:
			case LEFT_PAREN:
			case LEFT_BRACE:
				enterOuterAlt(_localctx, 2);
				{
				setState(368);
				expr5();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class Expr5Context extends ParserRuleContext {
		public Expr5Context expr5() {
			return getRuleContext(Expr5Context.class,0);
		}
		public TerminalNode MINUS_FLOAT() { return getToken(BKITParser.MINUS_FLOAT, 0); }
		public TerminalNode MINUS_INT() { return getToken(BKITParser.MINUS_INT, 0); }
		public Expr6Context expr6() {
			return getRuleContext(Expr6Context.class,0);
		}
		public Expr5Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr5; }
	}

	public final Expr5Context expr5() throws RecognitionException {
		Expr5Context _localctx = new Expr5Context(_ctx, getState());
		enterRule(_localctx, 70, RULE_expr5);
		int _la;
		try {
			setState(374);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MINUS_INT:
			case MINUS_FLOAT:
				enterOuterAlt(_localctx, 1);
				{
				setState(371);
				_la = _input.LA(1);
				if ( !(_la==MINUS_INT || _la==MINUS_FLOAT) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(372);
				expr5();
				}
				break;
			case ID:
			case INT_LIT:
			case FLOAT_LIT:
			case BOOL_LIT:
			case STRING_LIT:
			case LEFT_PAREN:
			case LEFT_BRACE:
				enterOuterAlt(_localctx, 2);
				{
				setState(373);
				expr6();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class Expr6Context extends ParserRuleContext {
		public Expr7Context expr7() {
			return getRuleContext(Expr7Context.class,0);
		}
		public Index_opContext index_op() {
			return getRuleContext(Index_opContext.class,0);
		}
		public Expr6Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr6; }
	}

	public final Expr6Context expr6() throws RecognitionException {
		Expr6Context _localctx = new Expr6Context(_ctx, getState());
		enterRule(_localctx, 72, RULE_expr6);
		try {
			setState(380);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(376);
				expr7();
				setState(377);
				index_op();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(379);
				expr7();
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

	public static class Expr7Context extends ParserRuleContext {
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public Expr8Context expr8() {
			return getRuleContext(Expr8Context.class,0);
		}
		public Expr7Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr7; }
	}

	public final Expr7Context expr7() throws RecognitionException {
		Expr7Context _localctx = new Expr7Context(_ctx, getState());
		enterRule(_localctx, 74, RULE_expr7);
		try {
			setState(384);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(382);
				function_call();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(383);
				expr8();
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

	public static class Expr8Context extends ParserRuleContext {
		public OperandContext operand() {
			return getRuleContext(OperandContext.class,0);
		}
		public TerminalNode LEFT_PAREN() { return getToken(BKITParser.LEFT_PAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RIGHT_PAREN() { return getToken(BKITParser.RIGHT_PAREN, 0); }
		public Expr8Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr8; }
	}

	public final Expr8Context expr8() throws RecognitionException {
		Expr8Context _localctx = new Expr8Context(_ctx, getState());
		enterRule(_localctx, 76, RULE_expr8);
		try {
			setState(391);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
			case INT_LIT:
			case FLOAT_LIT:
			case BOOL_LIT:
			case STRING_LIT:
			case LEFT_BRACE:
				enterOuterAlt(_localctx, 1);
				{
				setState(386);
				operand();
				}
				break;
			case LEFT_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(387);
				match(LEFT_PAREN);
				setState(388);
				expr();
				setState(389);
				match(RIGHT_PAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
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
		public Var_non_initContext var_non_init() {
			return getRuleContext(Var_non_initContext.class,0);
		}
		public Primitive_dataContext primitive_data() {
			return getRuleContext(Primitive_dataContext.class,0);
		}
		public Composite_dataContext composite_data() {
			return getRuleContext(Composite_dataContext.class,0);
		}
		public OperandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operand; }
	}

	public final OperandContext operand() throws RecognitionException {
		OperandContext _localctx = new OperandContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_operand);
		try {
			setState(396);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(393);
				var_non_init();
				}
				break;
			case INT_LIT:
			case FLOAT_LIT:
			case BOOL_LIT:
			case STRING_LIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(394);
				primitive_data();
				}
				break;
			case LEFT_BRACE:
				enterOuterAlt(_localctx, 3);
				{
				setState(395);
				composite_data();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class Function_callContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode LEFT_PAREN() { return getToken(BKITParser.LEFT_PAREN, 0); }
		public TerminalNode RIGHT_PAREN() { return getToken(BKITParser.RIGHT_PAREN, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public Function_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_call; }
	}

	public final Function_callContext function_call() throws RecognitionException {
		Function_callContext _localctx = new Function_callContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_function_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(398);
			match(ID);
			setState(399);
			match(LEFT_PAREN);
			setState(410);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ID) | (1L << INT_LIT) | (1L << FLOAT_LIT) | (1L << BOOL_LIT) | (1L << STRING_LIT) | (1L << MINUS_INT) | (1L << MINUS_FLOAT) | (1L << NOT) | (1L << LEFT_PAREN) | (1L << LEFT_BRACE))) != 0)) {
				{
				{
				setState(400);
				expr();
				setState(405);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(401);
					match(COMMA);
					setState(402);
					expr();
					}
					}
					setState(407);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				}
				setState(412);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(413);
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

	public static class Index_opContext extends ParserRuleContext {
		public TerminalNode LEFT_BRACKET() { return getToken(BKITParser.LEFT_BRACKET, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RIGHT_BRACKET() { return getToken(BKITParser.RIGHT_BRACKET, 0); }
		public Index_opContext index_op() {
			return getRuleContext(Index_opContext.class,0);
		}
		public Index_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_index_op; }
	}

	public final Index_opContext index_op() throws RecognitionException {
		Index_opContext _localctx = new Index_opContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_index_op);
		try {
			setState(424);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(415);
				match(LEFT_BRACKET);
				setState(416);
				expr();
				setState(417);
				match(RIGHT_BRACKET);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(419);
				match(LEFT_BRACKET);
				setState(420);
				expr();
				setState(421);
				match(RIGHT_BRACKET);
				setState(422);
				index_op();
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 31:
			return expr1_sempred((Expr1Context)_localctx, predIndex);
		case 32:
			return expr2_sempred((Expr2Context)_localctx, predIndex);
		case 33:
			return expr3_sempred((Expr3Context)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr1_sempred(Expr1Context _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr2_sempred(Expr2Context _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr3_sempred(Expr3Context _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3M\u01ad\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3"+
		"\2\3\2\3\2\7\2Z\n\2\f\2\16\2]\13\2\3\2\7\2`\n\2\f\2\16\2c\13\2\3\2\3\2"+
		"\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4q\n\4\3\4\3\4\3\4\3\4\3\4"+
		"\7\4x\n\4\f\4\16\4{\13\4\3\4\7\4~\n\4\f\4\16\4\u0081\13\4\3\4\3\4\3\4"+
		"\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\5\b\u0091\n\b\3\b\3\b\3\b"+
		"\5\b\u0096\n\b\7\b\u0098\n\b\f\b\16\b\u009b\13\b\3\b\3\b\3\t\3\t\5\t\u00a1"+
		"\n\t\3\t\3\t\3\t\5\t\u00a6\n\t\7\t\u00a8\n\t\f\t\16\t\u00ab\13\t\3\n\3"+
		"\n\3\13\3\13\3\13\3\13\6\13\u00b3\n\13\r\13\16\13\u00b4\3\13\5\13\u00b8"+
		"\n\13\3\f\3\f\3\f\3\f\5\f\u00be\n\f\3\f\6\f\u00c1\n\f\r\f\16\f\u00c2\3"+
		"\r\3\r\5\r\u00c7\n\r\3\r\3\r\3\r\5\r\u00cc\n\r\3\16\3\16\3\16\3\16\3\17"+
		"\3\17\3\17\3\17\3\20\3\20\3\20\7\20\u00d9\n\20\f\20\16\20\u00dc\13\20"+
		"\3\21\3\21\3\21\7\21\u00e1\n\21\f\21\16\21\u00e4\13\21\3\21\7\21\u00e7"+
		"\n\21\f\21\16\21\u00ea\13\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3"+
		"\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00ff\n\22"+
		"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u010a\n\23\f\23\16"+
		"\23\u010d\13\23\3\23\3\23\5\23\u0111\n\23\3\23\3\23\3\23\3\24\3\24\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30"+
		"\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\5\34\u013f\n\34\3\35"+
		"\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3 \3 \5 \u014e\n \3!\3!\3"+
		"!\3!\3!\3!\7!\u0156\n!\f!\16!\u0159\13!\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u0161"+
		"\n\"\f\"\16\"\u0164\13\"\3#\3#\3#\3#\3#\3#\7#\u016c\n#\f#\16#\u016f\13"+
		"#\3$\3$\3$\5$\u0174\n$\3%\3%\3%\5%\u0179\n%\3&\3&\3&\3&\5&\u017f\n&\3"+
		"\'\3\'\5\'\u0183\n\'\3(\3(\3(\3(\3(\5(\u018a\n(\3)\3)\3)\5)\u018f\n)\3"+
		"*\3*\3*\3*\3*\7*\u0196\n*\f*\16*\u0199\13*\7*\u019b\n*\f*\16*\u019e\13"+
		"*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u01ab\n+\3+\2\5@BD,\2\4\6\b\n\f"+
		"\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRT\2\b\3"+
		"\2\4\7\3\2)\63\3\2\'(\3\2\35 \4\2!!#%\3\2\37 \2\u01af\2[\3\2\2\2\4f\3"+
		"\2\2\2\6j\3\2\2\2\b\u0085\3\2\2\2\n\u0089\3\2\2\2\f\u008b\3\2\2\2\16\u008d"+
		"\3\2\2\2\20\u00a0\3\2\2\2\22\u00ac\3\2\2\2\24\u00b7\3\2\2\2\26\u00b9\3"+
		"\2\2\2\30\u00c6\3\2\2\2\32\u00cd\3\2\2\2\34\u00d1\3\2\2\2\36\u00d5\3\2"+
		"\2\2 \u00e2\3\2\2\2\"\u00fe\3\2\2\2$\u0100\3\2\2\2&\u0115\3\2\2\2(\u0117"+
		"\3\2\2\2*\u0124\3\2\2\2,\u012b\3\2\2\2.\u0132\3\2\2\2\60\u0136\3\2\2\2"+
		"\62\u0138\3\2\2\2\64\u013a\3\2\2\2\66\u013c\3\2\2\28\u0140\3\2\2\2:\u0144"+
		"\3\2\2\2<\u0146\3\2\2\2>\u014d\3\2\2\2@\u014f\3\2\2\2B\u015a\3\2\2\2D"+
		"\u0165\3\2\2\2F\u0173\3\2\2\2H\u0178\3\2\2\2J\u017e\3\2\2\2L\u0182\3\2"+
		"\2\2N\u0189\3\2\2\2P\u018e\3\2\2\2R\u0190\3\2\2\2T\u01aa\3\2\2\2VW\5\4"+
		"\3\2WX\7<\2\2XZ\3\2\2\2YV\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\a\3"+
		"\2\2\2][\3\2\2\2^`\5\6\4\2_^\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2bd\3"+
		"\2\2\2ca\3\2\2\2de\7\2\2\3e\3\3\2\2\2fg\7\30\2\2gh\7:\2\2hi\5\20\t\2i"+
		"\5\3\2\2\2jk\7\23\2\2kl\7:\2\2lp\7\3\2\2mn\7\25\2\2no\7:\2\2oq\5\36\20"+
		"\2pm\3\2\2\2pq\3\2\2\2qr\3\2\2\2rs\7\b\2\2sy\7:\2\2tu\5&\24\2uv\7<\2\2"+
		"vx\3\2\2\2wt\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z\177\3\2\2\2{y\3\2"+
		"\2\2|~\5\"\22\2}|\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2"+
		"\2\u0080\u0082\3\2\2\2\u0081\177\3\2\2\2\u0082\u0083\7\17\2\2\u0083\u0084"+
		"\7;\2\2\u0084\7\3\2\2\2\u0085\u0086\7\3\2\2\u0086\u0087\7>\2\2\u0087\u0088"+
		"\5\16\b\2\u0088\t\3\2\2\2\u0089\u008a\t\2\2\2\u008a\13\3\2\2\2\u008b\u008c"+
		"\5\16\b\2\u008c\r\3\2\2\2\u008d\u0090\78\2\2\u008e\u0091\5\n\6\2\u008f"+
		"\u0091\5\f\7\2\u0090\u008e\3\2\2\2\u0090\u008f\3\2\2\2\u0091\u0099\3\2"+
		"\2\2\u0092\u0095\7=\2\2\u0093\u0096\5\n\6\2\u0094\u0096\5\f\7\2\u0095"+
		"\u0093\3\2\2\2\u0095\u0094\3\2\2\2\u0096\u0098\3\2\2\2\u0097\u0092\3\2"+
		"\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a"+
		"\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009d\79\2\2\u009d\17\3\2\2\2"+
		"\u009e\u00a1\5\24\13\2\u009f\u00a1\5\30\r\2\u00a0\u009e\3\2\2\2\u00a0"+
		"\u009f\3\2\2\2\u00a1\u00a9\3\2\2\2\u00a2\u00a5\7=\2\2\u00a3\u00a6\5\24"+
		"\13\2\u00a4\u00a6\5\30\r\2\u00a5\u00a3\3\2\2\2\u00a5\u00a4\3\2\2\2\u00a6"+
		"\u00a8\3\2\2\2\u00a7\u00a2\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2"+
		"\2\2\u00a9\u00aa\3\2\2\2\u00aa\21\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ad"+
		"\7\3\2\2\u00ad\23\3\2\2\2\u00ae\u00b2\7\3\2\2\u00af\u00b0\7\66\2\2\u00b0"+
		"\u00b1\7\4\2\2\u00b1\u00b3\7\67\2\2\u00b2\u00af\3\2\2\2\u00b3\u00b4\3"+
		"\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b8\3\2\2\2\u00b6"+
		"\u00b8\7\3\2\2\u00b7\u00ae\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\25\3\2\2"+
		"\2\u00b9\u00c0\7\3\2\2\u00ba\u00bd\7\66\2\2\u00bb\u00be\5\26\f\2\u00bc"+
		"\u00be\7\4\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be\u00bf\3\2"+
		"\2\2\u00bf\u00c1\7\67\2\2\u00c0\u00ba\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2"+
		"\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\27\3\2\2\2\u00c4\u00c7\5\26\f"+
		"\2\u00c5\u00c7\5\22\n\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7"+
		"\u00c8\3\2\2\2\u00c8\u00cb\7>\2\2\u00c9\u00cc\5\f\7\2\u00ca\u00cc\5\n"+
		"\6\2\u00cb\u00c9\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\31\3\2\2\2\u00cd\u00ce"+
		"\5\26\f\2\u00ce\u00cf\7>\2\2\u00cf\u00d0\5\16\b\2\u00d0\33\3\2\2\2\u00d1"+
		"\u00d2\5\22\n\2\u00d2\u00d3\7>\2\2\u00d3\u00d4\5\n\6\2\u00d4\35\3\2\2"+
		"\2\u00d5\u00da\5\24\13\2\u00d6\u00d7\7=\2\2\u00d7\u00d9\5\24\13\2\u00d8"+
		"\u00d6\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db\3\2"+
		"\2\2\u00db\37\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd\u00de\5&\24\2\u00de\u00df"+
		"\7<\2\2\u00df\u00e1\3\2\2\2\u00e0\u00dd\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2"+
		"\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e8\3\2\2\2\u00e4\u00e2\3\2"+
		"\2\2\u00e5\u00e7\5\"\22\2\u00e6\u00e5\3\2\2\2\u00e7\u00ea\3\2\2\2\u00e8"+
		"\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9!\3\2\2\2\u00ea\u00e8\3\2\2\2"+
		"\u00eb\u00ff\5$\23\2\u00ec\u00ff\5(\25\2\u00ed\u00ff\5*\26\2\u00ee\u00ff"+
		"\5,\27\2\u00ef\u00f0\5.\30\2\u00f0\u00f1\7<\2\2\u00f1\u00ff\3\2\2\2\u00f2"+
		"\u00f3\5\60\31\2\u00f3\u00f4\7<\2\2\u00f4\u00ff\3\2\2\2\u00f5\u00f6\5"+
		"\62\32\2\u00f6\u00f7\7<\2\2\u00f7\u00ff\3\2\2\2\u00f8\u00f9\5\64\33\2"+
		"\u00f9\u00fa\7<\2\2\u00fa\u00ff\3\2\2\2\u00fb\u00fc\5\66\34\2\u00fc\u00fd"+
		"\7<\2\2\u00fd\u00ff\3\2\2\2\u00fe\u00eb\3\2\2\2\u00fe\u00ec\3\2\2\2\u00fe"+
		"\u00ed\3\2\2\2\u00fe\u00ee\3\2\2\2\u00fe\u00ef\3\2\2\2\u00fe\u00f2\3\2"+
		"\2\2\u00fe\u00f5\3\2\2\2\u00fe\u00f8\3\2\2\2\u00fe\u00fb\3\2\2\2\u00ff"+
		"#\3\2\2\2\u0100\u0101\7\24\2\2\u0101\u0102\5> \2\u0102\u0103\7\27\2\2"+
		"\u0103\u010b\5 \21\2\u0104\u0105\7\r\2\2\u0105\u0106\5> \2\u0106\u0107"+
		"\7\27\2\2\u0107\u0108\5 \21\2\u0108\u010a\3\2\2\2\u0109\u0104\3\2\2\2"+
		"\u010a\u010d\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u0110"+
		"\3\2\2\2\u010d\u010b\3\2\2\2\u010e\u010f\7\f\2\2\u010f\u0111\5 \21\2\u0110"+
		"\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0113\7\16"+
		"\2\2\u0113\u0114\7;\2\2\u0114%\3\2\2\2\u0115\u0116\5\4\3\2\u0116\'\3\2"+
		"\2\2\u0117\u0118\7\22\2\2\u0118\u0119\7\64\2\2\u0119\u011a\58\35\2\u011a"+
		"\u011b\7=\2\2\u011b\u011c\5:\36\2\u011c\u011d\7=\2\2\u011d\u011e\5<\37"+
		"\2\u011e\u011f\7\65\2\2\u011f\u0120\7\13\2\2\u0120\u0121\5 \21\2\u0121"+
		"\u0122\7\20\2\2\u0122\u0123\7;\2\2\u0123)\3\2\2\2\u0124\u0125\7\31\2\2"+
		"\u0125\u0126\5> \2\u0126\u0127\7\13\2\2\u0127\u0128\5 \21\2\u0128\u0129"+
		"\7\21\2\2\u0129\u012a\7;\2\2\u012a+\3\2\2\2\u012b\u012c\7\13\2\2\u012c"+
		"\u012d\5 \21\2\u012d\u012e\7\31\2\2\u012e\u012f\5> \2\u012f\u0130\7\34"+
		"\2\2\u0130\u0131\7;\2\2\u0131-\3\2\2\2\u0132\u0133\5\24\13\2\u0133\u0134"+
		"\7>\2\2\u0134\u0135\5> \2\u0135/\3\2\2\2\u0136\u0137\7\t\2\2\u0137\61"+
		"\3\2\2\2\u0138\u0139\7\n\2\2\u0139\63\3\2\2\2\u013a\u013b\5R*\2\u013b"+
		"\65\3\2\2\2\u013c\u013e\7\26\2\2\u013d\u013f\5> \2\u013e\u013d\3\2\2\2"+
		"\u013e\u013f\3\2\2\2\u013f\67\3\2\2\2\u0140\u0141\5\22\n\2\u0141\u0142"+
		"\7>\2\2\u0142\u0143\5> \2\u01439\3\2\2\2\u0144\u0145\5> \2\u0145;\3\2"+
		"\2\2\u0146\u0147\5> \2\u0147=\3\2\2\2\u0148\u0149\5@!\2\u0149\u014a\t"+
		"\3\2\2\u014a\u014b\5@!\2\u014b\u014e\3\2\2\2\u014c\u014e\5@!\2\u014d\u0148"+
		"\3\2\2\2\u014d\u014c\3\2\2\2\u014e?\3\2\2\2\u014f\u0150\b!\1\2\u0150\u0151"+
		"\5B\"\2\u0151\u0157\3\2\2\2\u0152\u0153\f\4\2\2\u0153\u0154\t\4\2\2\u0154"+
		"\u0156\5B\"\2\u0155\u0152\3\2\2\2\u0156\u0159\3\2\2\2\u0157\u0155\3\2"+
		"\2\2\u0157\u0158\3\2\2\2\u0158A\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u015b"+
		"\b\"\1\2\u015b\u015c\5D#\2\u015c\u0162\3\2\2\2\u015d\u015e\f\4\2\2\u015e"+
		"\u015f\t\5\2\2\u015f\u0161\5D#\2\u0160\u015d\3\2\2\2\u0161\u0164\3\2\2"+
		"\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163C\3\2\2\2\u0164\u0162"+
		"\3\2\2\2\u0165\u0166\b#\1\2\u0166\u0167\5F$\2\u0167\u016d\3\2\2\2\u0168"+
		"\u0169\f\4\2\2\u0169\u016a\t\6\2\2\u016a\u016c\5F$\2\u016b\u0168\3\2\2"+
		"\2\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016eE"+
		"\3\2\2\2\u016f\u016d\3\2\2\2\u0170\u0171\7&\2\2\u0171\u0174\5F$\2\u0172"+
		"\u0174\5H%\2\u0173\u0170\3\2\2\2\u0173\u0172\3\2\2\2\u0174G\3\2\2\2\u0175"+
		"\u0176\t\7\2\2\u0176\u0179\5H%\2\u0177\u0179\5J&\2\u0178\u0175\3\2\2\2"+
		"\u0178\u0177\3\2\2\2\u0179I\3\2\2\2\u017a\u017b\5L\'\2\u017b\u017c\5T"+
		"+\2\u017c\u017f\3\2\2\2\u017d\u017f\5L\'\2\u017e\u017a\3\2\2\2\u017e\u017d"+
		"\3\2\2\2\u017fK\3\2\2\2\u0180\u0183\5R*\2\u0181\u0183\5N(\2\u0182\u0180"+
		"\3\2\2\2\u0182\u0181\3\2\2\2\u0183M\3\2\2\2\u0184\u018a\5P)\2\u0185\u0186"+
		"\7\64\2\2\u0186\u0187\5> \2\u0187\u0188\7\65\2\2\u0188\u018a\3\2\2\2\u0189"+
		"\u0184\3\2\2\2\u0189\u0185\3\2\2\2\u018aO\3\2\2\2\u018b\u018f\5\24\13"+
		"\2\u018c\u018f\5\n\6\2\u018d\u018f\5\f\7\2\u018e\u018b\3\2\2\2\u018e\u018c"+
		"\3\2\2\2\u018e\u018d\3\2\2\2\u018fQ\3\2\2\2\u0190\u0191\7\3\2\2\u0191"+
		"\u019c\7\64\2\2\u0192\u0197\5> \2\u0193\u0194\7=\2\2\u0194\u0196\5> \2"+
		"\u0195\u0193\3\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198"+
		"\3\2\2\2\u0198\u019b\3\2\2\2\u0199\u0197\3\2\2\2\u019a\u0192\3\2\2\2\u019b"+
		"\u019e\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019f\3\2"+
		"\2\2\u019e\u019c\3\2\2\2\u019f\u01a0\7\65\2\2\u01a0S\3\2\2\2\u01a1\u01a2"+
		"\7\66\2\2\u01a2\u01a3\5> \2\u01a3\u01a4\7\67\2\2\u01a4\u01ab\3\2\2\2\u01a5"+
		"\u01a6\7\66\2\2\u01a6\u01a7\5> \2\u01a7\u01a8\7\67\2\2\u01a8\u01a9\5T"+
		"+\2\u01a9\u01ab\3\2\2\2\u01aa\u01a1\3\2\2\2\u01aa\u01a5\3\2\2\2\u01ab"+
		"U\3\2\2\2\'[apy\177\u0090\u0095\u0099\u00a0\u00a5\u00a9\u00b4\u00b7\u00bd"+
		"\u00c2\u00c6\u00cb\u00da\u00e2\u00e8\u00fe\u010b\u0110\u013e\u014d\u0157"+
		"\u0162\u016d\u0173\u0178\u017e\u0182\u0189\u018e\u0197\u019c\u01aa";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}