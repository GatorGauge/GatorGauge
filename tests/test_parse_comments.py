
""" Testcases for comment parsing """
import parse_comments as pc

JAVA_SOURCE = """
//comment_1
// comment_2
 // comment_3
  // comment_4
   // comment_5
    // comment_6
     // comment_7
      // comment_8
       // comment_9
	// comment_10_tab

}//comment_11
} //comment_12
} // comment_13
return "// comment_14";

/*comment_15*/
/* comment_16*/
/* comment_17 */

/* comment_18
*/

/*
comment_19
*/

/*
 * comment_20
 */

/**
 * javadoc
 */
"""


def test_comment_bol():
    """ comment at beginning-of-line """
    comments = pc.list_singleline_java_comments(JAVA_SOURCE)
    assert "comment_1" in comments
    assert "comment_2" in comments


def test_comment_space_indented_bol():
    """ BOL comment indented with spaces """
    comments = pc.list_singleline_java_comments(JAVA_SOURCE)
    assert "comment_3" in comments
    assert "comment_4" in comments
    assert "comment_5" in comments
    assert "comment_6" in comments
    assert "comment_7" in comments
    assert "comment_8" in comments
    assert "comment_9" in comments


def test_comment_tab_indented_bol():
    """ BOL comment indented with tabs """
    comments = pc.list_singleline_java_comments(JAVA_SOURCE)
    assert "comment_10_tab" in comments


def test_comment_eol():
    """ comment at end-of-line """
    comments = pc.list_singleline_java_comments(JAVA_SOURCE)
    assert "comment_11" in comments
    assert "comment_12" in comments
    assert "comment_13" in comments


def test_quoted_comment():
    """ comment within quoted string """
    comments = pc.list_singleline_java_comments(JAVA_SOURCE)
    assert "comment_14" not in comments


def test_multiline_singleline():
    """ multiline comment on singleline """
    comments = pc.list_multiline_java_comments(JAVA_SOURCE)
    assert "comment_15" in comments
    assert "comment_16" in comments
    assert "comment_17" in comments


def test_multiline_twoline():
    """ multiline comment across two lines """
    comments = pc.list_multiline_java_comments(JAVA_SOURCE)
    assert "comment_18" in comments


def test_multiline_tripleline():
    """ multiline comment across three lines """
    comments = pc.list_multiline_java_comments(JAVA_SOURCE)
    assert "comment_19" in comments
    assert "comment_20" in comments


def test_count_comments():
    """ check all comments are caught """
    singleline_comments = pc.list_singleline_java_comments(JAVA_SOURCE)
    multiline_comments = pc.list_multiline_java_comments(JAVA_SOURCE)
    javadoc_comments = pc.list_javadoc_comments(JAVA_SOURCE)
    assert len(singleline_comments) == 13
    assert len(multiline_comments) == 6
    assert len(javadoc_comments) == 1


def test_javadoc_comments():
    """ check that javadoc comments are caught """
    assert "javadoc" not in pc.list_multiline_java_comments(JAVA_SOURCE)
    assert "javadoc" not in pc.list_singleline_java_comments(JAVA_SOURCE)
    assert "javadoc" in pc.list_javadoc_comments(JAVA_SOURCE)


def test_get_all_comments():
    """ check that destructured get_all_comments parts are correct """
    singleline_comments = pc.list_singleline_java_comments(JAVA_SOURCE)
    multiline_comments = pc.list_multiline_java_comments(JAVA_SOURCE)
    javadoc_comments = pc.list_javadoc_comments(JAVA_SOURCE)
    assert pc.get_all_comments([JAVA_SOURCE]) == (
        singleline_comments,
        multiline_comments,
        javadoc_comments)


def test_get_avg_num_of_comments():
    """ check that averages make sense """
    avg_comments = pc.get_avg_nums_of_comments([JAVA_SOURCE, JAVA_SOURCE])
    assert avg_comments["javadoc"] == 1.0
    assert avg_comments["multiline"] == 6.0
    assert avg_comments["singleline"] == 13.0
