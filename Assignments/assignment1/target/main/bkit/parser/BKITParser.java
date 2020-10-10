// Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
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
		ARRAY_LIT=1, INT_ARRAY=2, FLOAT_ARRAY=3, STRING_ARRAY=4, ID=5, ILLEGAL_ESCAPE=6, 
		UNCLOSE_STRING=7, COMMENT=8, UNTERMINATED_COMMENT=9, ERROR_CHAR=10, WS=11, 
		Integer_literal=12, Float_literal=13, Boolean_literal=14, String_literal=15, 
		BODY=16, BREAK=17, CONTINUE=18, DO=19, ELSE=20, ELSELF=21, ELSEIF=22, 
		ENDBODY=23, ENDFOR=24, ENDWHILE=25, FOR=26, FUNCTION=27, IF=28, PARAMETER=29, 
		RETURN=30, THEN=31, VAR=32, WHILE=33, TRUE=34, FALSE=35, ENDDO=36, PLUS_INT=37, 
		PLUS_FLOAT=38, MINUS_INT=39, MINUS_FLOAT=40, STAR_INT=41, STAR_FLOAT=42, 
		DIV_INT=43, DIV_FLOAT=44, MOD=45, NOT=46, AND=47, OR=48, EQUAL=49, NOT_EQUAL_INT=50, 
		LESS_INT=51, GREATER_INT=52, LESS_OR_EQUAL_INT=53, GREATER_OR_EQUAL_INT=54, 
		NOT_EQUAL_FLOAT=55, LESS_FLOAT=56, GREATER_FLOAT=57, LESS_OR_EQUAL_FLOAT=58, 
		GREATER_OR_EQUAL_FLOAT=59, LEFT_PAREN=60, RIGHT_PARENT=61, LEFT_BRACKET=62, 
		RIGHT_BRACKET=63, LEFT_BRACE=64, RIGHT_BRACE=65, COLON=66, DOT=67, SEMI=68, 
		COMMA=69, ASSIGN=70;
	public static final int
		RULE_program = 0, RULE_var_declare = 1, RULE_function_declare = 2, RULE_primitive_type = 3, 
		RULE_composite_type = 4, RULE_bool_op = 5, RULE_int_op = 6, RULE_float_op = 7, 
		RULE_if_stmt = 8, RULE_while_stmt = 9, RULE_dowhile_stmt = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "var_declare", "function_declare", "primitive_type", "composite_type", 
			"bool_op", "int_op", "float_op", "if_stmt", "while_stmt", "dowhile_stmt"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
			"'ElSelf'", "'ElseIf'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", 
			"'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
			"'True'", "'False'", "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", "'*'", 
			"'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
			"'<'", "'>'", "'<='", "'>='", "'=\\='", "'<.'", "'>.'", "'<=.'", "'>=.'", 
			"'('", "')'", "'['", "']'", "'{'", "'}'", "':'", "'.'", "';'", "','", 
			"'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ARRAY_LIT", "INT_ARRAY", "FLOAT_ARRAY", "STRING_ARRAY", "ID", 
			"ILLEGAL_ESCAPE", "UNCLOSE_STRING", "COMMENT", "UNTERMINATED_COMMENT", 
			"ERROR_CHAR", "WS", "Integer_literal", "Float_literal", "Boolean_literal", 
			"String_literal", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSELF", 
			"ELSEIF", "ENDBODY", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
			"RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "PLUS_INT", 
			"PLUS_FLOAT", "MINUS_INT", "MINUS_FLOAT", "STAR_INT", "STAR_FLOAT", "DIV_INT", 
			"DIV_FLOAT", "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL_INT", "LESS_INT", 
			"GREATER_INT", "LESS_OR_EQUAL_INT", "GREATER_OR_EQUAL_INT", "NOT_EQUAL_FLOAT", 
			"LESS_FLOAT", "GREATER_FLOAT", "LESS_OR_EQUAL_FLOAT", "GREATER_OR_EQUAL_FLOAT", 
			"LEFT_PAREN", "RIGHT_PARENT", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", 
			"RIGHT_BRACE", "COLON", "DOT", "SEMI", "COMMA", "ASSIGN"
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
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(24); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(24);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case VAR:
					{
					setState(22);
					var_declare();
					}
					break;
				case FUNCTION:
					{
					setState(23);
					function_declare();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(26); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==FUNCTION || _la==VAR );
			setState(28);
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
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public Var_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_declare; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitVar_declare(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Var_declareContext var_declare() throws RecognitionException {
		Var_declareContext _localctx = new Var_declareContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_var_declare);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			match(VAR);
			setState(31);
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
		public TerminalNode FUNCTION() { return getToken(BKITParser.FUNCTION, 0); }
		public List<TerminalNode> COLON() { return getTokens(BKITParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(BKITParser.COLON, i);
		}
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode PARAMETER() { return getToken(BKITParser.PARAMETER, 0); }
		public TerminalNode BODY() { return getToken(BKITParser.BODY, 0); }
		public TerminalNode ENDBODY() { return getToken(BKITParser.ENDBODY, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public Function_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_declare; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitFunction_declare(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Function_declareContext function_declare() throws RecognitionException {
		Function_declareContext _localctx = new Function_declareContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_function_declare);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			match(FUNCTION);
			setState(34);
			match(COLON);
			setState(35);
			match(ID);
			setState(36);
			match(PARAMETER);
			setState(37);
			match(BODY);
			setState(38);
			match(COLON);
			setState(39);
			match(ENDBODY);
			setState(40);
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

	public static class Primitive_typeContext extends ParserRuleContext {
		public TerminalNode Integer_literal() { return getToken(BKITParser.Integer_literal, 0); }
		public TerminalNode Float_literal() { return getToken(BKITParser.Float_literal, 0); }
		public TerminalNode String_literal() { return getToken(BKITParser.String_literal, 0); }
		public TerminalNode Boolean_literal() { return getToken(BKITParser.Boolean_literal, 0); }
		public Primitive_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitive_type; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitPrimitive_type(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Primitive_typeContext primitive_type() throws RecognitionException {
		Primitive_typeContext _localctx = new Primitive_typeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_primitive_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Integer_literal) | (1L << Float_literal) | (1L << Boolean_literal) | (1L << String_literal))) != 0)) ) {
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

	public static class Composite_typeContext extends ParserRuleContext {
		public TerminalNode ARRAY_LIT() { return getToken(BKITParser.ARRAY_LIT, 0); }
		public Composite_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_composite_type; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitComposite_type(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Composite_typeContext composite_type() throws RecognitionException {
		Composite_typeContext _localctx = new Composite_typeContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_composite_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			match(ARRAY_LIT);
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

	public static class Bool_opContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(BKITParser.NOT, 0); }
		public TerminalNode AND() { return getToken(BKITParser.AND, 0); }
		public TerminalNode OR() { return getToken(BKITParser.OR, 0); }
		public Bool_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bool_op; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitBool_op(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Bool_opContext bool_op() throws RecognitionException {
		Bool_opContext _localctx = new Bool_opContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_bool_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NOT) | (1L << AND) | (1L << OR))) != 0)) ) {
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

	public static class Int_opContext extends ParserRuleContext {
		public TerminalNode PLUS_INT() { return getToken(BKITParser.PLUS_INT, 0); }
		public TerminalNode MINUS_INT() { return getToken(BKITParser.MINUS_INT, 0); }
		public TerminalNode STAR_INT() { return getToken(BKITParser.STAR_INT, 0); }
		public TerminalNode DIV_INT() { return getToken(BKITParser.DIV_INT, 0); }
		public TerminalNode MOD() { return getToken(BKITParser.MOD, 0); }
		public TerminalNode EQUAL() { return getToken(BKITParser.EQUAL, 0); }
		public TerminalNode NOT_EQUAL_INT() { return getToken(BKITParser.NOT_EQUAL_INT, 0); }
		public TerminalNode LESS_INT() { return getToken(BKITParser.LESS_INT, 0); }
		public TerminalNode GREATER_INT() { return getToken(BKITParser.GREATER_INT, 0); }
		public TerminalNode LESS_OR_EQUAL_INT() { return getToken(BKITParser.LESS_OR_EQUAL_INT, 0); }
		public TerminalNode GREATER_OR_EQUAL_INT() { return getToken(BKITParser.GREATER_OR_EQUAL_INT, 0); }
		public Int_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int_op; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitInt_op(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Int_opContext int_op() throws RecognitionException {
		Int_opContext _localctx = new Int_opContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_int_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PLUS_INT) | (1L << MINUS_INT) | (1L << STAR_INT) | (1L << DIV_INT) | (1L << MOD) | (1L << EQUAL) | (1L << NOT_EQUAL_INT) | (1L << LESS_INT) | (1L << GREATER_INT) | (1L << LESS_OR_EQUAL_INT) | (1L << GREATER_OR_EQUAL_INT))) != 0)) ) {
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

	public static class Float_opContext extends ParserRuleContext {
		public TerminalNode PLUS_FLOAT() { return getToken(BKITParser.PLUS_FLOAT, 0); }
		public TerminalNode MINUS_FLOAT() { return getToken(BKITParser.MINUS_FLOAT, 0); }
		public TerminalNode STAR_FLOAT() { return getToken(BKITParser.STAR_FLOAT, 0); }
		public TerminalNode DIV_FLOAT() { return getToken(BKITParser.DIV_FLOAT, 0); }
		public TerminalNode NOT_EQUAL_FLOAT() { return getToken(BKITParser.NOT_EQUAL_FLOAT, 0); }
		public TerminalNode LESS_FLOAT() { return getToken(BKITParser.LESS_FLOAT, 0); }
		public TerminalNode GREATER_FLOAT() { return getToken(BKITParser.GREATER_FLOAT, 0); }
		public TerminalNode LESS_OR_EQUAL_FLOAT() { return getToken(BKITParser.LESS_OR_EQUAL_FLOAT, 0); }
		public TerminalNode GREATER_OR_EQUAL_FLOAT() { return getToken(BKITParser.GREATER_OR_EQUAL_FLOAT, 0); }
		public Float_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_float_op; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitFloat_op(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Float_opContext float_op() throws RecognitionException {
		Float_opContext _localctx = new Float_opContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_float_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PLUS_FLOAT) | (1L << MINUS_FLOAT) | (1L << STAR_FLOAT) | (1L << DIV_FLOAT) | (1L << NOT_EQUAL_FLOAT) | (1L << LESS_FLOAT) | (1L << GREATER_FLOAT) | (1L << LESS_OR_EQUAL_FLOAT) | (1L << GREATER_OR_EQUAL_FLOAT))) != 0)) ) {
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

	public static class If_stmtContext extends ParserRuleContext {
		public If_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_stmt; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitIf_stmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final If_stmtContext if_stmt() throws RecognitionException {
		If_stmtContext _localctx = new If_stmtContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_if_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
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
		public While_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_stmt; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitWhile_stmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final While_stmtContext while_stmt() throws RecognitionException {
		While_stmtContext _localctx = new While_stmtContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
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
		public Dowhile_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dowhile_stmt; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitDowhile_stmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Dowhile_stmtContext dowhile_stmt() throws RecognitionException {
		Dowhile_stmtContext _localctx = new Dowhile_stmtContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_dowhile_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3H=\4\2\t\2\4\3\t\3"+
		"\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f"+
		"\t\f\3\2\3\2\6\2\33\n\2\r\2\16\2\34\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n"+
		"\3\13\3\13\3\f\3\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24\26\2\6\3\2\16\21"+
		"\3\2\60\62\b\2\'\'))++--//\638\7\2((**,,..9=\2\63\2\32\3\2\2\2\4 \3\2"+
		"\2\2\6#\3\2\2\2\b,\3\2\2\2\n.\3\2\2\2\f\60\3\2\2\2\16\62\3\2\2\2\20\64"+
		"\3\2\2\2\22\66\3\2\2\2\248\3\2\2\2\26:\3\2\2\2\30\33\5\4\3\2\31\33\5\6"+
		"\4\2\32\30\3\2\2\2\32\31\3\2\2\2\33\34\3\2\2\2\34\32\3\2\2\2\34\35\3\2"+
		"\2\2\35\36\3\2\2\2\36\37\7\2\2\3\37\3\3\2\2\2 !\7\"\2\2!\"\7F\2\2\"\5"+
		"\3\2\2\2#$\7\35\2\2$%\7D\2\2%&\7\7\2\2&\'\7\37\2\2\'(\7\22\2\2()\7D\2"+
		"\2)*\7\31\2\2*+\7E\2\2+\7\3\2\2\2,-\t\2\2\2-\t\3\2\2\2./\7\3\2\2/\13\3"+
		"\2\2\2\60\61\t\3\2\2\61\r\3\2\2\2\62\63\t\4\2\2\63\17\3\2\2\2\64\65\t"+
		"\5\2\2\65\21\3\2\2\2\66\67\3\2\2\2\67\23\3\2\2\289\3\2\2\29\25\3\2\2\2"+
		":;\3\2\2\2;\27\3\2\2\2\4\32\34";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}